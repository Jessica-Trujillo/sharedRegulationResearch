# Author: Jessica Trujillo
# Date: April 15, 2022
# V.1.0

from asyncio.windows_events import NULL
from Indicators.indicatorInterface import *

class DictionaryCounter(IndicatorInterface):
    contents = NULL

    def getFilePath(self) -> str:
        return "unknown"
    def count(self, p) -> int:
        if self.contents == NULL:
            path = self.getFilePath()
            file = open(path,"r")
            containingWords = set()
            for word in file.read().split():
                containingWords.add(word)
            self.contents = containingWords
            

        count = 0
        for item in p.postItems:
            if item in self.contents:
                count = count + 1
        return count

    def getType(self) -> str:
        return "unkown"