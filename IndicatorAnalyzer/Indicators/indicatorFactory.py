from Indicators.indicatorInterface import *
from Indicators.negativewordcounter import *
from Indicators.positivewordcounter import *

def createIndicators() -> list[IndicatorInterface]:
    rtnList = []
    rtnList.append(NegativeWordIndicator())
    rtnList.append(PositiveWordIndicator())
    return rtnList