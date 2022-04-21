# Author: Jessica Trujillo
# Date: April 15, 2022
# V.1.0

from PostParser.jsonpost import *

def parsePost(postContents) -> JsonPost:
  

    body = postContents["body"]
    newPost = JsonPost()
    newPost.message = body

    newPost.id = postContents["id"]
    newPost.score = postContents["score"]
    newPost.author = postContents["author"]



    parts = body.split()
    newPost.postItems = parts

    return newPost

