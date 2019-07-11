import requests
from bs4 import BeautifulSoup
import pandas as pd         #for transposing csv
import csv                  #for transposing csv

# symbols and columns
symbols = open("symbol.txt").read().strip().replace("\"", "").split(",")
columns = ['Open:', 'High:', 'Beta:', 'Shares Out:', 'Total Shares (All Classes):', 'Prev. Close:', 'Low:', 'VWAP:', 'Market Cap:', 'Market Cap (All Classes)*:', 'Dividend:', 'Div. Frequency:', 'P/E Ratio:', 'EPS:', 'Yield:', 'Ex-Div Date:', 'P/B Ratio:', 'Exchange:']

# a list of lists to store all the data(numbers) from webscraping
data_list = []

# this is the range, use this for test else you will get an error when building the df
# simply change this to n = len(symbol) if want to use the whole thing
n = 20

for i in range(n):
    url = "https://web.tmxmoney.com/quote.php?qm_symbol="+ symbols[i]
    print(url)
    page = requests.get(url)

    # parse webpage with BeautifulSoup, get tags with class "detailed-quote-table'
    soup = BeautifulSoup(page.text, "html.parser")
    detailed_quote_tables = soup.findAll(class_="detailed-quote-table")

    # clean data into list format with only numbers
    detailed_quotes_list = [dq.get_text() for dq in detailed_quote_tables]
    detailed_quotes_string = ''.join(detailed_quotes_list)
    detailed_quotes_list = detailed_quotes_string.split('\n')
    detailed_quotes_list = list(filter(None, detailed_quotes_list))[1::2]

    data_list.append(detailed_quotes_list)

# create a DataFrame to store the data, which is like a table
df = pd.DataFrame(data_list, columns=columns, index=[symbols[:n]])

# the below is to print the DataFrame
# pd.set_option('display.max_columns', None)
# print(df.head())

# export DataFrame to csv
df.to_csv('data.csv')
