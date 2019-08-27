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

# prepares empty file with header
open('data.csv', 'w').close()       #Erase old fild

def get_req(url):
    headers = {"User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    try:
        req = requests.get(url, timeout=10, headers=headers)
    except Exception as e:
        print(e)
        print("Pause for 15s")
        time.sleep(15)
        req = get_req(url)
    return req

#Print header
f = open("data.csv", "a")
for i in range(len(columns)):
    f.write("Symbol,"+columns[i])

print("#","\t\t\t","URL","\t\t\t   ","elapsed_time")
for i in range(n_start, n):
    start_time = time.time()
    url = "https://web.tmxmoney.com/quote.php?qm_symbol="+symbols[i]
    req = get_req(url)
    # parse webpage with BeautifulSoup, get tags with class "detailed-quote-table'
    parse = BeautifulSoup(req.text, "html.parser")
    detailed_quote_tables = parse.findAll(class_="dq-card")
    detailed_quotes_list = [dq.get_text() for dq in detailed_quote_tables]
    detailed_quotes_string = ''.join(detailed_quotes_list)
    detailed_quotes = detailed_quotes_string
    #Replace all the crazy shit
    detailed_quotes = detailed_quotes.replace('<div class="dq-card">', '', 1)
    detailed_quotes = detailed_quotes.replace('Prev. Close', '', 1)
    detailed_quotes = detailed_quotes.replace('Dividend', '', 1)
    detailed_quotes = detailed_quotes.replace('Yield', '', 1)
    detailed_quotes = detailed_quotes.replace('Exchange', '', 1)
    detailed_quotes = detailed_quotes.replace('Open:', '', 1)
    detailed_quotes = detailed_quotes.replace('High', '', 1)
    detailed_quotes = detailed_quotes.replace('Beta', '', 1)
    detailed_quotes = detailed_quotes.replace('Shares Out.', '', 1)
    detailed_quotes = detailed_quotes.replace('Total Shares (All Classes)', '', 1)
    detailed_quotes = detailed_quotes.replace('Low', '', 1)
    detailed_quotes = detailed_quotes.replace('Market Cap', '', 1)
    detailed_quotes = detailed_quotes.replace('Market Cap (All Classes)*', '', 1)
    detailed_quotes = detailed_quotes.replace('Div. Frequency', '', 1)
    detailed_quotes = detailed_quotes.replace('P/E Ratio', '', 1)
    detailed_quotes = detailed_quotes.replace('EPS', '', 1)
    detailed_quotes = detailed_quotes.replace('Ex-Div Date', '', 1)
    detailed_quotes = detailed_quotes.replace('P/B Ratio', '', 1)
    detailed_quotes = detailed_quotes.replace('VWAP', '', 1)
    detailed_quotes = detailed_quotes.replace('	', '')
    detailed_quotes = detailed_quotes.replace('\n', '')
    detailed_quotes = detailed_quotes.replace(',', '')
    detailed_quotes = detailed_quotes.replace(':', ',')
    detailed_quotes = detailed_quotes.replace('\r', '')
    detailed_quotes = detailed_quotes.replace('N/A', '-')
    #Convert to text
    for a in range(n_start, n):
        temps = ""
    f = open("data.csv", "a")
    f.write("\n"+symbols[i]+","+detailed_quotes)
    #Print timelaps and General info
    elapsed_time = time.time() - start_time
    print(i, url,"\t","%.2f" % elapsed_time)
