import pandas as pd
import requests
from bs4 import BeautifulSoup

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

html_data= requests.get(url).text

beautiful_soup=BeautifulSoup(html_data,'html5lib')

tables = beautiful_soup.find_all('table')
table=tables[1]

tesla_revenue= pd.DataFrame(columns=["Date", "Revenue"])

for row in table.find("tbody").find_all("tr"):
    col= row.find_all("td")
    date=col[0].text
    revenue=col[1].text

    tesla_revenue=tesla_revenue._append({"Date":date, "Revenue":revenue},ignore_index=True)

# removes 
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",","")
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("|","")
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("\ ","")
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$","")
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]

print(tesla_revenue.tail())