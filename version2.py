import requests
import re                   #replace betweeen 2 strings
from bs4 import BeautifulSoup
import ast                  #cant remember why imported
import pandas as pd         #for transposing csv
import csv                  #for transposing csv
import itertools            #this works  #from itertools import izip  #this doesnt work because it cant fint izip but can zip?
from collections import deque


#While loop to get the data from all 2274 symbols in a single file
a = 0
symbol = open("symbol.txt").read().strip().replace("\"", "").split(",")

for i in range(2): #len(symbol)
    url = "https://web.tmxmoney.com/quote.php?qm_symbol="+ symbol[i]
    print(url)
    page = requests.get(url)

    # parse webpage with BeautifulSoup, get tags with class "detailed-quote-table'
    soup = BeautifulSoup(page.text, "html.parser")
    detailed_quote_tables = soup.findAll(class_="detailed-quote-table")

    # clean data into list format
    detailed_quotes_text_list = [dq.get_text() for dq in detailed_quote_tables]
    detailed_quotes_string = ''.join(detailed_quotes_text_list)
    detailed_quotes = detailed_quotes_string.split('\n\n')

    # remove empty element
    for dq in detailed_quotes:
        if dq == '':
            detailed_quotes.remove(dq)

    # clean data for csv format, like change line-break to comman etc
    # this part is slow (because of string creation) so should find a better way

    for j in range(len(detailed_quotes)):
        # detailed_quotes[i] = detailed_quotes[i].replace('Prev. Close:', 'Prev. Close:,', 1)
        # detailed_quotes[i] = detailed_quotes[i].replace('Dividend:', 'Dividend:,', 1)
        # detailed_quotes[i] = detailed_quotes[i].replace('Yield:', 'Yield:,', 1)
        # detailed_quotes[i] = detailed_quotes[i].replace('Exchange:', 'Exchange:,', 1)
        detailed_quotes[i] = detailed_quotes[i].replace('\t', '')
        detailed_quotes[i] = detailed_quotes[i].replace('\n', ',')
        detailed_quotes[i] = detailed_quotes[i].replace(',', '')
        detailed_quotes[i] = detailed_quotes[i].replace(':', ',,')
        detailed_quotes[i] = detailed_quotes[i].replace('Open,', 'Open', 1)
        if i > 0:
            detailed_quotes[i] = detailed_quotes[i].replace(',', '', 1)

    #Transpose data
    names = []
    values = []

    #Output check system
    ##i = 0
    ##while i < 100:
    ##    print(detailed_quotes[i]+"\n")
    ##    i =i+ 1

    # write data to file
    with open("C:\\Users\\kevin\\Desktop\\python file exsports\\soup.csv", "w") as f:           #"w" for write and "a" for append
        f.write('\n'.join(detailed_quotes))


print(detailed_quotes)
