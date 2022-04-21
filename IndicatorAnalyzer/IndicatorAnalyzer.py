# Author: Jessica Trujillo
# Date: April 15, 2022
# V.1.0

from asyncio.windows_events import NULL

from Indicators.indicatorFactory import *
from PostParser.postparser import *
from redditjsonserializer import *
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import os
import json
import xlwt
from xlwt import Workbook

joinedPath = currentLocation + "\\Resources\\NewPosts\\RC_2020-01-17\RC_2020-01-17"
#joinedPath = currentLocation + "\\Resources\\NewPosts\\RC_2007-01\\RC_2007-01"

workbook = Workbook()
workbook.add_sheet('Posts')
sheet = workbook.get_sheet(0)



file = open(joinedPath, "r")

bySubreddit = parseRedditJsonBySubreddit(file)

allIndicators = createIndicators()
sheet.write(0, 0, "Subreddit")
sheet.write(0, 1, "Positive")
sheet.write(0, 2, "Negative")
sheet.write(0, 3, "Average Post Length")
sheet.write(0, 4, "Total Posts")

c = 1
for subRedditKey in bySubreddit:
    value = bySubreddit[subRedditKey]

    positivePosts = 0
    negativePosts = 0
    neutralPosts = 0
    
    currentAverage = 0
    currentCount = 0
    totalPosts = 0
    
    for post in value:
        indicationsByType = {
            
        }
        indicationsByType["Positive"] = 0
        indicationsByType["Negative"] = 0
        newCount = len(post.postItems)

        dif = newCount - currentAverage
        currentCount = currentCount + 1

        difToAdd= dif / currentCount
        currentAverage += difToAdd      

        for ind in allIndicators:
            count = ind.count(post)
            
            currentCount = indicationsByType[ind.getType()]
            currentCount += count
            indicationsByType[ind.getType()] = currentCount

        post.posWords = indicationsByType["Positive"]
        post.negWords = indicationsByType["Negative"]
        
        if post.posWords > post.negWords:
            positivePosts += 1
        if post.negWords > post.posWords:
            negativePosts += 1
        if post.negWords == post.posWords:
            neutralPosts += 1
        totalPosts += 1
    print("SubReddit: " + str(subRedditKey) + "-- " + str(positivePosts) + " positive posts, " + str(negativePosts) + " negative posts, " + str(neutralPosts) + " neutral posts " + str(currentAverage) + " average post length")
    
    sheet.write(c, 0, str(subRedditKey))
    sheet.write(c, 1, positivePosts)
    sheet.write(c, 2, negativePosts)
    sheet.write(c, 3, currentAverage)
    sheet.write(c, 4, totalPosts)
    
    c = c + 1


workbook.save("C:\\ResearchPaper\\IndicatorAnalyzer\\output.xls")
