import analyzeKenoData
import random
#This is a test using least frequent numbers

#Theory using this test is that by picking the least shown numbers, you can get a reasonable N-Spot draw
def test1(testFile, spots):
    maxDraw = 200
    minDraw = 0
    numCount = analyzeKenoData.numFreq(testFile,minDraw,maxDraw)
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
        if (numCount[num-1] >= (barrier*.9)):
            zeros.remove(num)
    return analyzeKenoData.checkNums(testFile, maxDraw, 10, uncommon[:spots])

#Pick three random numbers from uncommon pool
def test2(testFile, spots):
    maxDraw = 200
    minDraw = 0
    numCount = analyzeKenoData.numFreq(testFile,minDraw,maxDraw)
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
        if (numCount[num-1] >= (barrier*.9)):
            zeros.remove(num)
    #Pick 3 random ones from group if more than 3 elements in uncommon
    if len(uncommon) > spots:
        sample = random.sample(uncommon, 3)
    return analyzeKenoData.checkNums(testFile, maxDraw, 10, sample[:spots])

#Use zeros and supplment with uncommon(ordered)
def test3(testFile, spots):
    maxDraw = 200
    minDraw = 0
    numCount = analyzeKenoData.numFreq(testFile,minDraw,maxDraw)
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
        if (numCount[num-1] >= (barrier*.9)):
            zeros.remove(num)
    if len(zeros) >= spots:
        return analyzeKenoData.checkNums(testFile, maxDraw, 10, zeros[:spots])
    if len(zeros) < spots:
        for x in range(0, spots-len(zeros)):
            zeros.append(uncommon[x])
        return analyzeKenoData.checkNums(testFile, maxDraw, 10, zeros[:spots])
#Use common numbers instead
def test4(testFile, spots):
    maxDraw = 200
    minDraw = 0
    numCount = analyzeKenoData.numFreq(testFile,minDraw,maxDraw)
    #Get most common and least common numbers
    common = analyzeKenoData.mostFreq(numCount)
    uncommon = analyzeKenoData.leastFreq(numCount)
    #Get the numbers that have not appeared in the last 10 games
    zeroCount = analyzeKenoData.numFreq(testFile,maxDraw-10 ,maxDraw)
    zeros = analyzeKenoData.zeroFreq(zeroCount)
    #Remove numbers in all arrays that appeared more than 25% of the time
    return analyzeKenoData.checkNums(testFile, maxDraw, 10, common[:spots])
