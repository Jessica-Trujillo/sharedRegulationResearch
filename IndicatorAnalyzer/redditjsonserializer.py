# Author: Jessica Trujillo
# Date: April 15, 2022
# V.1.0

import json
from PostParser.postparser import *

def parseRedditJsonBySubreddit(file) -> dict:
    bySubreddit = dict() 

    while 1 == 1:
        data = file.readline()
        if data == '':
            break
        try:
            dataAsJson = json.loads(data)

            body = dataAsJson["body"]
            if body == "[removed]":
                continue

            newPost = parsePost(dataAsJson)
            
            subReddit = dataAsJson["subreddit"]
            if subReddit not in bySubreddit:
                bySubreddit[subReddit] = []
            bySubreddit[subReddit].append(newPost)
        except:
            continue
    return bySubreddit
