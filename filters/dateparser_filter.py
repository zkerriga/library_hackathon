from Date import *
from .utils import (greenPrint, redPrint)
from typing import Final

import sys

sys.path.append("../dateparser/dateparser")
from dateparser import dateparser


def dateParserFilter(sourceStr: str, dateObj: Date):
	parsedObj: Final = dateparser.parse(
		sourceStr,
		languages=['ru'],
		settings={
			'RELATIVE_BASE': getDefaultDateTimeObj()
		}
	)
	if parsedObj:
		dateObj.setTimeFromDateTimeObj(parsedObj)
		greenPrint("DateParserFilter -> " + str(parsedObj) + f" -> {sourceStr}")
