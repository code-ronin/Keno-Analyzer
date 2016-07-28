import re
from itertools import islice
from collections import Counter
import random

#Calculate frequency of numbers currently on text file
def numFreq(textFile):
    #Grab numbers from text file
    numList = []
    data = open(textFile, 'r')
    regex = re.compile(r'(\d{2})')
    for line in data:
        numbers = regex.findall(line)
        for nums in numbers:
            numList.append(int(nums))
    #Get frequency of numbers for the list
    numCount = []
    for i in range(1, 81):
        numCount.append(numList.count(i))
    print(numCount)
    #Total draws Currently:
    with open(textFile) as f:
      print ("Total draws: " + str(len(f.readlines())))
    #Hot numbers: Numbers that have not shown up frequently
    print("Hottest Number: " + str(numCount.index(min(numCount))+1))
    #Cold Numbers: Numbers that have appeared most often
    print("Coldest Number: " + str(numCount.index(max(numCount))+1))
    #Numbers that have shown up in the last N games
    N = 15  #Number of games that occur within an hour
    with open(textFile) as f:
        s = f.readlines()
    s.reverse()
    s = s[:N]
    hotNumList = []
    for i in range(0,N):
        hotNums = regex.findall(s[i])
        for nums in hotNums:
            hotNumList.append(int(nums))
    hotNumCount = []
    for i in range(1, 81):
        hotNumCount.append(hotNumList.count(i))
    print(hotNumCount)
    #Numbers that have not appeared in the past N games
    zeroArr = [i for i, x in enumerate(hotNumCount) if x == 0]
    zeroArr = [x+1 for x in zeroArr]
    print "These numbers have not appeared in the past ", str(N) ," games: ", str(zeroArr)
    #Top 4 numbers that have appeared the most in the last N games
    test = sorted(range(len(hotNumCount)), key=lambda i: hotNumCount[i], reverse=True)[:4]
    print ("These are the top four numbers of the past " +
    str(N) + " games: " + str(test))

#Analyze past data and see what would have been the
#best single number as well as the best drawing period
'''
To do this, you just need count all numbers for a certain
grouping, and grab the maximum
'''
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
    '''
    print("*********RUNNING-Pick2**************")
    skipN = 10    #Number of draws starting from 1 to skip
    N = 10     #Number od draws you are looking at after skip
    tempList1 = []
    tempList2 = []
    currPick2 = []
    tempPick = []
    numCounter = {}
    bestCount = 0
    with open(textFile) as f:
        data = f.readlines()[skipN:]
    regex = re.compile(r'(\d{2})')
    for i in range(0,N):
        numList = []
        numbers = regex.findall(data[i])
        #Convert strings into nums First
        for nums in numbers:
            numList.append(int(nums))
        #Populate test arrays
        if not tempList1:
            for nums in numList:
                tempList1.append(nums)
        elif not tempList2: #Populate list 2
            print("*********Populating list 2...")
            for nums in numList:
                tempList2.append(nums)
            print(tempList1)
            print(tempList2)
            currPick2 = [x for x in tempList1 if x in tempList2]
            bestCount = 2
            for nums in currPick2:
                if nums in numCounter:
                    numCounter[nums] += 1
                else:
                    numCounter[nums] = 1
            print("First set is: " + str(currPick2))
        else:
            test = [x for x in currPick2 if x in numList]
            for nums in currPick2:
                if nums in numCounter:
                    numCounter[nums] += 1
                else:
                    numCounter[nums] = 1
            if not test:
                print("No cookie here")
            else:
                print("additional nums: " + str(test))
                bestCount += 1

    print("Best count was " + str(bestCount))
    print("numbers were " + str(currPick2))
    '''




    #Get biggest num


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



#Functions to simulate past history to test validity of prediction methods
#This assumes at least 150 games have already been played
#For simulating odds and return from picking 1
def sim1(textFile, drawNum):
    return textFile

#For simulating odds and return picking 2
def sim2(textFile, drawNum):
    return textFile
