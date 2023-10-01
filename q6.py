import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-06-14']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

# data
gma = yf.Ticker("GME")
gma_data = gma.history(period="max")
gma_data.reset_index(inplace=True)
gma_data = gma_data[['Date', 'Close']]

# revenue
url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"


html_data= requests.get(url).text

beautiful_soup=BeautifulSoup(html_data,'html5lib')

tables = beautiful_soup.find_all('table')
table=tables[1]

gme_revenue= pd.DataFrame(columns=["Date", "Revenue"])

for row in table.find("tbody").find_all("tr"):
    col= row.find_all("td")
    date=col[0].text
    revenue=col[1].text

    gme_revenue=gme_revenue._append({"Date":date, "Revenue":revenue},ignore_index=True)

gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(",","")
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("|","")
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("\ ","")
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("$","")

gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]

make_graph(gma_data, gme_revenue, "GameStop")