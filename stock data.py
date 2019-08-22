import pandas as pd         #for transposing csv
import time                 #for time counter

# prepares empty file with header
open('data3.csv', 'w').close()       #Erase old fild

# symbols and columns
symbols = open("symbol.txt").read().strip().split(",")

# parameters to scraping
n_start = 0
n = len(symbols)

for i in range(n_start, n):
    try:                            #Instead of doing this try and actually fix the errors because it skips like 50% of loops
        start_time = time.time()
        dfs = pd.read_html('https://ca.finance.yahoo.com/quote/'+symbols[i]+'.TO/history?p='+symbols[i]+'.TO',header=0)
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
        ListTotal = [Column1,Column2, Column3, Column4, Column5, Column6, Column7]
        header = ["Date","Open","High","Low","Close","Adj Close","Volume"]
        #print(str(lists[0]))
        for d in range(100):                #Manually typed in the number of rows because len(table) doesnt work
            Column1[d] = lists[d][0]
            Column2[d] = lists[d][1]
            Column3[d] = lists[d][2]
            Column4[d] = lists[d][3]
            Column5[d] = lists[d][4]
            Column6[d] = lists[d][5]
            Column7[d] = lists[d][6]
            #print(d,Column1[d],Column2[d],Column3[d],Column4[d],Column5[d],Column6[d],Column7[d])
        #Remove comma from first list
        for c in range(0,100):
            temp = str(Column1[c])
            temp=temp.replace(', 2019', '')
            Column1[c] = temp
        #Write to file in reverse order (oldest to newest)
        for a in range(0,7):
            f = open("data3.csv", "a")
            f.write(symbols[i]+",")
            f.write(header[a]+",")
            for b in range(99,0,-1):                    #Cant do 100 because it crashes for some reason
                f = open("data3.csv", "a")              #Has to be here or it wont write to file for some reasons even tho its also writen outside the loop
                f.write('%s' % ListTotal[a][b]+',')
            f.write("\r")
        #Print timelaps and General info
        elapsed_time = time.time() - start_time
        print(i, "\t","%.2f" % elapsed_time)
    except:
        pass
