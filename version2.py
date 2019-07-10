import requests
import re                   #replace betweeen 2 strings
from bs4 import BeautifulSoup
import ast                  #cant remember why imported
import pandas as pd         #for transposing csv
import csv                  #for transposing csv
import itertools            #this works
#from itertools import izip  #this doesnt work because it cant fint izip but can zip?


# get webpage in html (im also goin to make this a loop for one file for all the data)
url = "https://web.tmxmoney.com/quote.php?qm_symbol=BBD.A"
page = requests.get(url)
#companies =  = ["AAB", "AAY"] #ill turn this in a 1360 list and add it to the url as a download loop

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
        
for i in range(len(detailed_quotes)):
    detailed_quotes[i] = detailed_quotes[i].replace('Prev. Close:', 'Prev. Close:,', 1)
    detailed_quotes[i] = detailed_quotes[i].replace('Dividend:', 'Dividend:,', 1)
    detailed_quotes[i] = detailed_quotes[i].replace('Yield:', 'Yield:,', 1)
    detailed_quotes[i] = detailed_quotes[i].replace('Exchange:', 'Exchange:,', 1)
    detailed_quotes[i] = detailed_quotes[i].replace('\t', '')
    detailed_quotes[i] = detailed_quotes[i].replace('\n', ',')
    if i > 0:
        detailed_quotes[i] = detailed_quotes[i].replace(',', '', 1)

# write data to file
with open("C:\\Users\\kevin\\Desktop\\python file exsports\\soup.csv", "w") as f:
    f.write('\n'.join(detailed_quotes))
    #f.write('\n'.join(detailed_quotes))

print(detailed_quotes)
