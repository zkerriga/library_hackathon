import dateparser
from Date import *
from .utils import (green, red)

def dateParserFilter(sourceStr: str, dateObj: Date):
	parsedObj = dateparser.parse(sourceStr, languages=['ru'])
	if parsedObj:
		dateObj.setTimeFromDateTimeObj(parsedObj)
		green("DateParserFilter -> " + str(parsedObj) + f" -> {sourceStr}")
