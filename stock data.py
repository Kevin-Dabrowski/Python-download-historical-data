import requests
from bs4 import BeautifulSoup
import pandas as pd         #for transposing csv
import csv                  #for transposing csv
import time                 #for time counter
import urllib.request

header = [] * 100
dfs = pd.read_html('https://ca.finance.yahoo.com/quote/AAB.TO/history?p=AAB.TO',header=0)
for df in dfs:
    header = header[1]
    print(df)
