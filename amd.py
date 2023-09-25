
import pandas as pd
import json
import wget
import yfinance as yf

#wget.download("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json") 

amd = yf.Ticker("AMD")
with open('amd.json') as json_file:
     amd_info=json.load(json_file)
#print("Type:", type(amd_info))

#Question 1 Use the key 'country' to find the country the stock belongs to, remember it as it will be a quiz question.
print(amd_info['country']) #usa

#Question 2 Use the key 'sector' to find the sector the stock belongs to, remember it as it will be a quiz question.
print(amd_info['sector']) #Technology

#Question 3 Obtain stock data for AMD using the history function, set the period to max. Find the Volume traded on the first day (first row).
amd_d = amd.history(period="max")

print(amd_d) # 219600