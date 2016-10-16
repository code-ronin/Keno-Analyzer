import analyzeKenoData
#This is a test using least frequent numbers

#Theory using this test is that by picking the least shown numbers, you can get a reasonable N-Spot draw

def test1(testFile):
    maxDraw = 290
    minDraw = 0
    numCount = analyzeKenoData.numFreq(testFile,minDraw,maxDraw)
    print(numCount)
    #Get most common and least common numbers
    common = analyzeKenoData.mostFreq(numCount)
    uncommon = analyzeKenoData.leastFreq(numCount)
    #Get the numbers that have not appeared in the last 10 games
    zeroCount = analyzeKenoData.numFreq(testFile,maxDraw-10 ,maxDraw)
    zeros = analyzeKenoData.zeroFreq(zeroCount)
    #Remove numbers in all arrays that appeared more than 25% of the time
    barrier = maxDraw/4
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
