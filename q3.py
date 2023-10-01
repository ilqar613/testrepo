import yfinance as yf


gma = yf.Ticker("GME")

gma_data = gma.history(period="max")

gma_data.reset_index(inplace=True)

gma_data_head = gma_data.head()

print(gma_data_head)