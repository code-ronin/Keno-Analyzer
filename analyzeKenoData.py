from __future__ import division
import re
import os
from itertools import islice
from collections import Counter
import random
import betCalculator

#Get frequency of numbers, skipping some and counting up to N
def numFreq(textFile, skipN, N):
    #Grab numbers from text file
    numList = []
    with open(textFile) as f:
        data = f.readlines()[skipN:]
    regex = re.compile(r'(\d{2})')
    for i in range(0,(N-skipN)):
        numbers = regex.findall(data[i])
        for nums in numbers:
            numList.append(int(nums))
    #Get frequency of numbers for the list
    numCount = []
    for i in range(1, 81):
        numCount.append(numList.count(i))
    #Return list of nums
    return numCount

#Given input of numbers, check if full match
def checkNums(textFile, skipN, maxDraws, numList):
    #Read the next ten lines
    with open(textFile) as f:
        data = f.readlines()[skipN:]
    regex = re.compile(r'(\d{2})')
    for i in range(0,maxDraws):
        numbers = regex.findall(data[i])
        numbers = map(int, numbers)
        matches = len(set(numbers).intersection(numList))
        return betCalculator.matchPayout(len(numList), matches)


#Get the least frequent numbers
def leastFreq(numCount):
    bot4 = sorted(range(len(numCount)), key=lambda i: numCount[i], reverse=True)[74:81]
    #Add 1 to all top 4, as list starts count at 0, not 1
    bot4 = [x+1 for x in bot4]
    return sorted(bot4)

#Get the most frequent numbers
def mostFreq(numCount):
    top4 = sorted(range(len(numCount)), key=lambda i: numCount[i], reverse=True)[:6]
    #Add 1 to all top 4, as list starts count at 0, not 1
    top4 = [x+1 for x in top4]
    return sorted(top4)

#Get numbers that have not appeared
def zeroFreq(numCount):
    zeroArr = [i for i, x in enumerate(numCount) if x == 0]
    zeroArr = [x+1 for x in zeroArr]
    return zeroArr

#Get ratio of times number has shown up out of all possible chances
def ratioCalc(numCount, zeroArr, chances):
    ratioList =[]
    for num in zeroArr:
        numerator = numCount[num-1]
        ratioList.append(round(numerator/chances, 4))
    print(len(ratioList))
    return ratioList

#Find the longest combo that shows up the most
def bestPattern(textFile, skipN, N):
    #Return varaibles
    bestChain = []
    bestCount = 0
    startLoc = 0
    #Variables for holding best result
    currChain = []
    currCount = 0
    testChain = []
    with open(textFile) as f:
        data = f.readlines()[skipN:]
    regex = re.compile(r'(\d{2})')
    #By default, set current combo as the first set of numbers
    currChain = regex.findall(data[0])
    for i in range(1,(N-skipN)):
        testChain = regex.findall(data[i])
        #Get the intersection of numbers
        test = list(set(currChain).intersection(testChain))
        #Combo is less than 3, begin reset
        if(len(test) <= 2):
            if(currCount >= bestCount):
                bestChain = currChain
                bestCount = currCount
                startLoc = i
            currChain = testChain
            currCount = 0
        else:
            currChain = test
            currCount+=1

    #Return results
    print("StartLoc: " + str(startLoc))
    print("Chain count: " + str(bestCount))
    print("Best Chain: " + str(sorted(bestChain)))
    return bestChain


#####
def bestPick1(textFile):
    print("*********RUNNING-Pick1**************")
    skipN = 10    #Number of draws starting from 1 to skip
    N = 30     #Number od draws you are looking at after skip
    numList = []
    with open(textFile) as f:
        data = f.readlines()[skipN:]
    regex = re.compile(r'(\d{2})')
    for i in range(0,N):
        numbers = regex.findall(data[i])
        for nums in numbers:
            numList.append(int(nums))
    #Get biggest num
    numCount = []
    for i in range(1, 81):
        numCount.append(numList.count(i))
    print(numCount)
    print("Best single number: " + str(numCount.index(max(numCount))+1))
    print("Number of wins: " +  str(max(numCount)))
    print("Smallest loss count: " +  str(min(numCount)))
################

#Locate best set of picked numbers for N picks
def bestPickN(textFile, N):
    for i in range(1,7):
        skips = random.randint(0,270)
        #skips = 200
        draws = i*5
        print("*********RUNNING-Match " + str(draws) +" for Pick " + str(N)+"**************")
        num_counter = {}
        #skips = 156    #Number of draws starting from 1 to skip
        #draws = 30     #Number od draws you are looking at after skip
        numList = []
        with open(textFile) as f:
            data = f.readlines()[skips:]
        regex = re.compile(r'(\d{2})')
        for i in range(0, draws):
            numbers = regex.findall(data[i])
            for nums in numbers:
                numList.append(int(nums))
        numCount = []
        for i in range(1, 81):
            numCount.append(numList.count(i))
        #print(numCount)
        test = sorted(range(len(numCount)), key=lambda i: numCount[i], reverse=True)[:N]
        test = [x+1 for x in test]
        #Taking top N numbers, count games won
        wonGames = []
        for i in range(0, draws):
            numbers = regex.findall(data[i])
            numbers = map(int, numbers)
            count = 0
            for x in test:
                if x in numbers:
                    count += 1
            wonGames.append(count)
            #Put results in dict

        gameCount = Counter(wonGames)
        gameCount2 = sorted(gameCount.items())
        freq = reduce(lambda x, y: x + y, numCount) / len(numCount)
        print("Avg. frequency of nums: " + str(reduce(lambda x, y: x + y, numCount) / len(numCount)))
        print("Won games: " + str(gameCount2))
        print("Best Nums are " + str(test))

        #Calculate games won
        test2 = list(gameCount.values())
        keyVals = list(gameCount.keys())
        winNum = 0
        if (N < 3):
            for i in range(0,len(test2)):
                if keyVals[i] != 0:
                    winNum += test2[i]
        else:
            for i in range(2, len(test2)):
                if keyVals[i] > 1:
                    winNum += test2[i]

        print(str(winNum) + "/" + str(draws) + "," + str(gameCount2) + ",f" + str(freq))

###############
#Locate best set of picked numbers for N picks
def bbestPickN(textFile, N):
    print("*********RUNNING-Pick-" + str(N) +"**************")
    num_counter = {}
    skips = 156    #Number of draws starting from 1 to skip
    draws = 30     #Number od draws you are looking at after skip
    numList = []
    with open(textFile) as f:
        data = f.readlines()[skips:]
    regex = re.compile(r'(\d{2})')
    for i in range(0, draws):
        numbers = regex.findall(data[i])
        for nums in numbers:
            numList.append(int(nums))
    numCount = []
    for i in range(1, 81):
        numCount.append(numList.count(i))
    print(numCount)
    test = sorted(range(len(numCount)), key=lambda i: numCount[i], reverse=True)[:N]
    test = [x+1 for x in test]
    #Taking top N numbers, count games won
    wonGames = []
    for i in range(0, draws):
        numbers = regex.findall(data[i])
        numbers = map(int, numbers)
        count = 0
        for x in test:
            if x in numbers:
                count += 1
        wonGames.append(count)
        #Put results in dict

    gameCount = Counter(wonGames)
    print("Avg. frequency of nums: " + str(reduce(lambda x, y: x + y, numCount) / len(numCount)))
    print("Won games: " + str(sorted(gameCount.items())))
    print("Best Nums are " + str(test))



#Predict the next four winning numbers using current data
def predictNumbers(textFile):
    #Grab numbers from text file
    numList = []
    data = open(textFile, 'r')
    regex = re.compile(r'(\d{2})')
    for line in data:
        numbers = regex.findall(line)
        if not numList:     #Check if List is empty
            print("*********Populating New draw...")
            numList = numbers
            print(numList)
        else:
            numList = set(numList) & set(numbers)
            if not numList:
                print("*********Populating New draw...")
                numList = numbers
            print numList
    return textFile

#Get overall data
def scanAll(testDir):
    massArr = [0]*80
    fileCount = 0
    for filename in os.listdir(testDir):
        fileCount += 1
        blankArr = []
        fullPath = testDir+ '/' + filename
        blankArr = numFreq(fullPath)
        for i in range(0,80):
            massArr[i] += blankArr[i]
    #Calculate percentage that numbers show up
    #Assumes 300 draws a day
    baseLine = 300*fileCount
    print(massArr)
    return massArr

    '''
    for i in range (0,80):
        print(str(round((massArr[i]/baseLine), 3)))
    #print(massArr)
    '''

#Functions to simulate past history to test validity of prediction methods
#This assumes at least 150 games have already been played
#For simulating odds and return from picking 1
def sim1(textFile, drawNum):
    return textFile

#For simulating odds and return picking 2
def sim2(textFile, drawNum):
    return textFile
