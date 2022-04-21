# Author: Jessica Trujillo
# Date: April 15, 2022
# V.1.0

from Indicators.dictionarycounter import *
from globals import *

class PositiveWordIndicator(DictionaryCounter): 
    def getFilePath(self) -> str:
        return currentLocation + "\\Resources\\positive-words.txt"
    def getType(self) -> str:
        return "Positive"