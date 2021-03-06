from .present_filter import presentFilter
from .dateparser_filter import *
from .text_filter import textFilter
from .utils import (greenPrint, redPrint)
from .quarter import getQuarter


def convertStrToObjDate(strToConvert: str, dateObj):

	cleanStr = textFilter(strToConvert)

	if cleanStr.startswith("с "):
		cleanStr = cleanStr[2:]
	if not dateObj.isLocked():
		dateParserFilter(cleanStr, dateObj)
	if not dateObj.isLocked():
		presentFilter(cleanStr, dateObj)

def mainFilters(sourceList, datesList):
	print("[+] Filters started!")
	filtered: int = 0

	for sourceStr, dateObj in zip(sourceList, datesList):
		if " по " in sourceStr:
			listEndStartPeriod: list = sourceStr.split(" по ")
			startDateString: str = listEndStartPeriod[0]
			endDateString: str = listEndStartPeriod[1]
			convertStrToObjDate(startDateString, dateObj)
			endObjDate = Date()
			convertStrToObjDate(endDateString, endObjDate)
			dateObj.setDateToPeriod(endObjDate)
			greenPrint(f"Period Filter -> {sourceStr}")

		else:
			cleanStr = textFilter(sourceStr)

			quarter: tuple = getQuarter(cleanStr)
			if quarter:
				dateObj.setQuarter(quarter)

			convertStrToObjDate(cleanStr, dateObj)

		if dateObj.isLocked():
			filtered += 1
		elif sourceStr != cleanStr:
			redPrint(f"{sourceStr} -> {cleanStr}")
		else:
			redPrint(f"{sourceStr}")

	print(f"[+] Filtered {filtered} times! That is {round(filtered * 100 / len(sourceList))}%!")
	print("[+] Filters stopped!")
	return datesList
