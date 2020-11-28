import dateparser
from Date import *
from .utils import (greenPrint, redPrint)
from typing import Final

def dateParserFilter(sourceStr: str, dateObj: Date):
	parsedObj: Final = dateparser.parse(sourceStr, languages=['ru'])
	if parsedObj:
		dateObj.setTimeFromDateTimeObj(parsedObj)
		greenPrint("DateParserFilter -> " + str(parsedObj) + f" -> {sourceStr}")
