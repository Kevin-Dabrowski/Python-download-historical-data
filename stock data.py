import requests
from bs4 import BeautifulSoup
import pandas as pd         #for transposing csv
import csv                  #for transposing csv
import time                 #for time counter
import urllib.request

# prepares empty file with header
open('data3.txt', 'w').close()       #Erase old fild

header = [] * 100
dfs = pd.read_html('https://ca.finance.yahoo.com/quote/AAB.TO/history?p=AAB.TO',header=0)
for df in dfs:
    table = df.values.tolist()
lists = table
# Declare lists
Column1 = ["-"] * (len(lists)-1) #Removes last row which is weird text
Column2 = ["-"] * (len(lists)-1)
Column3 = ["-"] * (len(lists)-1)
Column4 = ["-"] * (len(lists)-1)
Column5 = ["-"] * (len(lists)-1)
Column6 = ["-"] * (len(lists)-1)
Column7 = ["-"] * (len(lists)-1)
print(str(lists[0]))
for d in range(100):                #Manually typed in the number of rows because len(table) doesnt work
    Column1[d] = lists[d][0]
    Column2[d] = lists[d][1]
    Column3[d] = lists[d][2]
    Column4[d] = lists[d][3]
    Column5[d] = lists[d][4]
    Column6[d] = lists[d][5]
    Column7[d] = lists[d][6]
    #print(Column1[d],Column2[d],Column3[d],Column4[d],Column5[d],Column6[d],Column7[d])
f = open("data3.txt", "a")
f.write(str(Column1[1]))
f.write("\n")

#print(str(lists[1][0]))


    
##    df.to_csv(r'C:\Users\kevin\Desktop\python file exsports\web-scraper-master\data3.csv')
##    f = open("data3.csv", "a")
##    f.write(str(df)+"\n")

