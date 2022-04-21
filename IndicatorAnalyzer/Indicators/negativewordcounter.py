# Author: Jessica Trujillo
# Date: April 15, 2022
# V.1.0

from Indicators.dictionarycounter import *
from globals import *

class NegativeWordIndicator(DictionaryCounter): 
    def getFilePath(self) -> str:
        return currentLocation + "\\Resources\\negative-words.txt"
    def getType(self) -> str:
        return "Negative"