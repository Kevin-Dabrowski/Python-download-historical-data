import requests
from bs4 import BeautifulSoup
import pandas as pd         #for transposing csv
import csv                  #for transposing csv
import time                 #for time counter

# symbols and columns
symbols = open("symbol.txt").read().strip().split(",")
columns = ['Open:', 'High:', 'Beta:', 'Shares Out:', 'Total Shares (All Classes):', 'Prev. Close:', 'Low:', 'VWAP:', 'Market Cap:', 'Market Cap (All Classes)*:', 'Dividend:', 'Div. Frequency:', 'P/E Ratio:', 'EPS:', 'Yield:', 'Ex-Div Date:', 'P/B Ratio:', 'Exchange:']

# parameters to scraping
buffer = 50
n_start = 0
n = len(symbols)

data_list = buffer*[None]
empty_columns = []
abnormal_columns = []

start_time = time.time()

# prepares empty file with header
df = pd.DataFrame(columns=columns)
df.to_csv('data.csv')

def save_to_file(data_list, index_start, index_end):
    df = pd.DataFrame(data_list, columns=columns, index=[symbols[index_start:index_end]])
    data_list = buffer*[None]
    with open('data.csv', 'a') as f:
        df.to_csv(f, mode='a', header=None)

def get_req(url):
    headers = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    try:
        req = requests.get(url, timeout=10, headers=headers)
    except Exception as e:
        print(e)
        print("Pause for 30s")
        time.sleep(30)
        req = get_req(url)
    return req
print("#","\t\t\t","URL","\t\t\t   ","elapsed_time")
for i in range(n_start, n):
    url = "https://web.tmxmoney.com/quote.php?qm_symbol="+symbols[i]
    req = get_req(url)

    # parse webpage with BeautifulSoup, get tags with class "detailed-quote-table'
    parse = BeautifulSoup(req.text, "html.parser")
    detailed_quote_tables = parse.findAll(class_="detailed-quote-table")

    # clean data into list format with only numbers
    detailed_quotes_list = [dq.get_text() for dq in detailed_quote_tables]
    detailed_quotes_string = ''.join(detailed_quotes_list)
    detailed_quotes_list = detailed_quotes_string.split('\n')
    detailed_quotes_list = list(filter(None, detailed_quotes_list))[1::2]

    elapsed_time = time.time() - start_time
    print(i, url,"\t","%.2f" % elapsed_time)

    # catch abnormal list
    if len(detailed_quotes_list) == 0:
        print("Empty quote")
        empty_columns.append(symbols[i])
    elif len(detailed_quotes_list) != 18:
        print("Abnormal column length:", len(detailed_quotes_list))
        abnormal_columns.append(symbols[i])
        detailed_quotes_list = []

    data_list[i % buffer] = detailed_quotes_list

    if (i + 1) % buffer == 0:
        print("saved items: ", i + 1)
        save_to_file(data_list, i - (buffer - 1), i + 1)

# create a DataFrame to store the data, which is like a table
# store leftover data
data_list = data_list[:n % buffer]
save_to_file(data_list, n - (n % buffer), n)

print("Companies with empty quotes", empty_columns)
print("Companies with abnormal columns", abnormal_columns)
