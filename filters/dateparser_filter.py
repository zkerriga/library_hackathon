import dateparser
from Date import *
from .utils import (greenPrint, redPrint)

def dateParserFilter(sourceStr: str, dateObj: Date):
	parsedObj = dateparser.parse(sourceStr, languages=['ru'])
	if parsedObj:
		dateObj.setTimeFromDateTimeObj(parsedObj)
		greenPrint("DateParserFilter -> " + str(parsedObj) + f" -> {sourceStr}")
