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
#yesteryear = kenoNumParser.getPastKeno(2014, "02", "14")
#print(yesteryear)


#Step 2: Analyze Collected Data
#Count number of occurances of numbers for that day
#kenoFile = 'kenoData/kenoNum07-12-2016.txt'
#analyzeKenoData.numFreq(kenoFile)
#analyzeKenoData.bestPick1(kenoFile)
analyzeKenoData.bestPickN(kenoFile, 3)
#For each

#test
#getKenoData.getTodayKeno()
