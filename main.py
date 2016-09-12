import getKenoData
import analyzeKenoData
from datetime import date
from calendar import monthrange

'''
Various triggers for certain things:
Trigger 1 = Gather data from single month
Trigger 2 = Keno Analysis
'''
trigger = 1
#Variables for large grab
year = 2015
month = "01"
if trigger == 1:
    #Calculate days in month that year
    days = monthrange(year,int(month))[1]
    for x in range(1, days+1):
        day = str(x)
        pastURL = getKenoData.getPastKenoURL(year, month, day)
        htmlFile = getKenoData.getKenoNums(pastURL)
        getKenoData.parseFile(htmlFile)
if trigger == 2:
    print("Test")
#Step 1: Get Data from MA Keno site
#Get Yesterday's URL
'''
today = date.today()
kenoURL = getKenoData.getYesterdayURL(today)
#Get Yesterday's Numbers
htmlFile = getKenoData.getKenoNums(kenoURL)
#Parse the HTML saved in the text file
kenoFile = getKenoData.parseFile(htmlFile)

'''
#Below is code to grab URL from the past
#will use later for mass data collection
#yesteryear = kenoNumParser.getPastKeno(2014, "02", "14")
#print(yesteryear)


#Step 2: Analyze Collected Data
#Count number of occurances of numbers for that day
#analyzeKenoData.numFreq(kenoFile)
#analyzeKenoData.bestPick1(kenoFile)
#Run the best pick data for a Pick-N
#analyzeKenoData.bestPickN(kenoFile, 3)

#test
#getKenoData.getTodayKeno()

#Step 3: Run overall analysis of data
#Numbers most currently represented
#analyzeKenoData.scanAll()

#Numbers most currently under-represented
