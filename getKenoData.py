from datetime import timedelta
from bs4 import BeautifulSoup
import sys
import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from calendar import monthrange
import os

#Function to get yesterday's Keno numbers
def getYesterdayURL(today):
    yesterday, date, day, month, year = "", "", "", "", ""
    yesterday = today - timedelta(1)
    date = yesterday.strftime("%x")
    day = yesterday.strftime("%d")
    month = yesterday.strftime("%m")
    year = yesterday.strftime("%Y")
    print("Grabbing all MA Keno numbers for " + date + "\n")
    kenoURL = ('http://www.masslottery.com/games/lottery/search/' +
    'results-history.html?game_id=15&mode=2&selected_date=' + year +
    '-'+ month + '-' + day)
    return kenoURL

#Function to get Keno URL for a specific date
def getPastKenoURL(year, month, day):
    print("Getting numbers for "+ str(month) + " of " + str(year))
    if int(day) < 10:
        kenoURL = ('http://www.masslottery.com/games/lottery/search/' +
        'results-history.html?game_id=15&mode=2&selected_date=' + str(year) +
        '-'+ month + '-0' + day)
    else:
        kenoURL = ('http://www.masslottery.com/games/lottery/search/' +
        'results-history.html?game_id=15&mode=2&selected_date=' + str(year) +
        '-'+ month + '-' + day)
    return kenoURL
####################
#Get today's currently printed Keno numbers
def getTodayKeno():
    #Go the the main MA Keno site
    print("Getting today's current numbers")
    kenoURL = 'http://www.masslottery.com/games/keno.html'
    browser = webdriver.Firefox()
    type(browser)
    browser.get(kenoURL)
    time.sleep(10)
    html2 = browser.execute_script("return document.documentElement.innerHTML;")
    soup = BeautifulSoup(html2, "html.parser")
    #Grab the minimum draw number for that day
    cleanSoup = soup.find('div', {'class': 'section_range'})
    cleanSoup = cleanSoup.findAll(text=re.compile(r'(\d{7})'))
    startNum = ' '.join(cleanSoup[0].string.split())
    endNum = ' '.join(cleanSoup[1].string.split())
    #Open URL to all draws currently drawn for today
    kenoURL = ('http://www.masslottery.com/games/lottery/search/results-todays.html?game_id=15&mode=0&min='
    + startNum + '&max=' + endNum)
    browser.get(kenoURL)
    time.sleep(10)
    html3 = browser.execute_script("return document.documentElement.innerHTML;")
    soup2 = BeautifulSoup(html3, "html.parser")
    table = soup2.find('table', {'class': 'zebra-body-only'})
    cleantable = table.findAll(text=re.compile('((\d{2}-){19}\d{2})'))
    '''
    sys.stdout = open('temptemp.txt', "w")
    print(cleantable)
    sys.stdout = sys.__stdout__
    '''
    #Grab all current numbers
    #currTime = time.strftime("%H%M%S")
    currDate = time.strftime("%d%m%Y")
    kenoFile = ("kenoData/kenoNum" + currDate + "-" + startNum + "-" + endNum +".txt")
    with open(kenoFile, "w+") as f:
        for matchNum in cleantable:
            f.write(' '.join(matchNum.string.split()) + '\n')
    #for matchNum in re.finditer('((\d{2}-){19}\d{2})', cleantable):
    #    print(matchNum.group(1))
    #startNum = soup.find('div', {'class': 'todays-numbers-wrapper'})
    #print(startNum)
    browser.quit()

#/html/body/form/div/div[2]/div[2]/input
#Get keno numbers from URL
def getKenoNums(URL):
    #Start Selenium driver to get HTML from inspect page option
    browser = webdriver.Firefox()
    type(browser)
    browser.get(URL)
    #Wait for page to load to have necessary HTML on page
    time.sleep(10)
    html2 = browser.execute_script("return document.documentElement.innerHTML;")
    #Save HTML to text file after refining it with BeautifulSoup
    soup = BeautifulSoup(html2, "html.parser")
    print("Saving numbers to text file...")
    htmlFile = "htmlFile.html"
    sys.stdout = open(htmlFile, "w")
    print(soup)
    #Redirect stdout to terminal from text file and close browser
    sys.stdout = sys.__stdout__
    print("Closing browser")
    browser.quit()
    return htmlFile

#Parse HTML file with Keno URL data
def parseFile(htmlFile):
    #Grab table in html file
    html = open(htmlFile)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table', {'class': 'zebra-body-only'})
    #Remove HTML material from table, and save text to tempText.txt file
    cleantable = table.findAll(text=True)
    sys.stdout = open('tempText.txt', 'w')
    print(cleantable)
    sys.stdout = sys.__stdout__
    #Open tempText.txt and parse out date and Keno numbers from .txt
    with open('tempText.txt', 'r') as myfile:
        data = myfile.read()
    matchDate = re.search('(\d{2}/\d{2}/\d{4})', data, re.I)
    cleanDate = matchDate.group().replace("/", "-")
    kenoFile = ("kenoData/kenoNum" + cleanDate + ".txt")
    #Store data in kenoFile
    with open(kenoFile, "w+") as f:
        for matchNum in re.finditer('((\d{2}-){19}\d{2})', data):
            f.write((matchNum.group(1))+"\n")
    #Delete the HTML file and tempText.txt file
    print("Removing temp files...")
    os.remove(htmlFile)
    os.remove('tempText.txt')
    return kenoFile
