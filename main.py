import getKenoData
import analyzeKenoData
from datetime import date

#Step 1: Get Data from MA Keno site
#Get Yesterday's URL
today = date.today()
kenoURL = getKenoData.getYesterdayURL(today)
#Get Yesterday's Numbers
htmlFile = getKenoData.getKenoNums(kenoURL)
#Parse the HTML saved in the text file
kenoFile = getKenoData.parseFile(htmlFile)

#Below is code to grab URL from the past
#will use later for mass data collection
#yesteryear = kenoNumParser.getPastKeno(2014, "02", "14")
#print(yesteryear)


#Step 2: Analyze Collected Data
#Count number of occurances of numbers for that day
#analyzeKenoData.numFreq(kenoFile)
#analyzeKenoData.bestPick1(kenoFile)
#Run the best pick data for a Pick-N
analyzeKenoData.bestPickN(kenoFile, 3)
#For each

#test
#getKenoData.getTodayKeno()

#Step 3: Update overall analysis of data
