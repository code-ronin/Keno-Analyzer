import sys
import getKenoData
import analyzeKenoData
import Tests
from datetime import date
from calendar import monthrange
import os


'''
Various triggers for certain things:
Trigger 1 = Gather data from single month
Trigger 2 = Keno Analysis using kenoData - figure out patterns here
Trigger 3 = Test analysis: using one day's data - use patterns found above
'''
trigger = 4
#Variables for large month grab
year = 2015
month = "02"
#Grab all keno numbers for a month in a year
if trigger == 1:
    #Check if month + year's data already available
    if(os.path.isfile('kenoData/kenoNum' + month + '-01-' + str(year) + '.txt')):
        print(month + " of " + str(year) + " already recorded")
        sys.exit(0)
    #Calculate days in month that year
    days = monthrange(year,int(month))[1]
    for x in range(1, days+1):
        day = str(x)
        pastURL = getKenoData.getPastKenoURL(year, month, day)
        htmlFile = getKenoData.getKenoNums(pastURL)
        getKenoData.parseFile(htmlFile)
#Run an overall analysis to test kenoData
if trigger == 2:
    print("Scanning kenoData...")
    testDir = 'kenoData'
    #Get frequency of all numbers in a directory
    largeArr = analyzeKenoData.scanAll(testDir)
    #Get most common numbers and most infrequent numbers



if trigger == 3:
    print("Checking data for accurate patterns")
    #testFile = 'kenoData/kenoNum07-13-2016.txt'
    testFile = 'kenoData/kenoNum07-25-2016.txt'
    print(testFile)
    #Grab a single text file
    #numCount = analyzeKenoData.numFreq(testFile,0,290)
    maxDraw = 290
    numCount = analyzeKenoData.numFreq(testFile,0,maxDraw)
    print(numCount)
    #Get most common and least common numbers
    common = analyzeKenoData.mostFreq(numCount)
    uncommon = analyzeKenoData.leastFreq(numCount)
    #Get the numbers that have not appeared in the last 10 games
    zeroCount = analyzeKenoData.numFreq(testFile,maxDraw-10 ,maxDraw)
    zeros = analyzeKenoData.zeroFreq(zeroCount)
    #Remove numbers in all arrays that appeared more than 25% of the time
    barrier = 290/4
    for num in reversed(common):
        if (numCount[num-1] >= (barrier*.9)):
            common.remove(num)
    for num in reversed(uncommon):
        if (numCount[num-1] >= (barrier*.9)):
            uncommon.remove(num)
    for num in reversed(zeros):
        print(num)
        if (numCount[num-1] >= (barrier*.9)):
            zeros.remove(num)
    #Print all arrays
    print("COMMON: ")
    print(common)
    print("UNCOMMON: ")
    print(uncommon)
    print("ZEROS: ")
    print(zeros)
    analyzeKenoData.checkNums(testFile, maxDraw, 10, uncommon[:3])
#Run test proven in 3 with
if trigger == 4:
    testFolder = 'kenoData/kenoNum01-2015'
    print("Testing with " + testFolder)
    #f_count = 0
    #t_count = 0
    for filename in os.listdir(testFolder):
        fullPath = (testFolder+'/'+filename)
        earnings = Tests.test4(fullPath, 4)
        print("EARNINGS: " + str(earnings))

'''
        if(Tests.test3(fullPath)):
            t_count+=1
        else:
            f_count+=1
    print("TRUE: "+ str(t_count))
    print("FALSE: " + str(f_count))
'''

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
