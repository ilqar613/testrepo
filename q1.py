
import yfinance as yf

tesla = yf.Ticker("TSLA")

tesla_data = tesla.history(period="max")

tesla_data.reset_index(inplace=True)

tesla_data_head = tesla_data.head()

print(tesla_data_head)