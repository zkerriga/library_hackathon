from .present_filter import presentFilter
from .dateparser_filter import *
from .text_filter import textFilter
from .utils import (greenPrint, redPrint)
from .quarter import getQuarter

def mainFilters(sourceList, datesList):
	print("[+] Filters started!")
	filtered: int = 0

	for sourceStr, dateObj in zip(sourceList, datesList):
		cleanStr = textFilter(sourceStr)

		quarter: tuple = getQuarter(cleanStr)
		if quarter:
			dateObj.setQuarter(quarter)

		if not dateObj.isLocked():
			dateParserFilter(cleanStr, dateObj)
		if not dateObj.isLocked():
			presentFilter(cleanStr, dateObj)

		if dateObj.isLocked():
			filtered += 1
		elif sourceStr != cleanStr:
			redPrint(f"{sourceStr} -> {cleanStr}")
		else:
			redPrint(f"{sourceStr}")

	print(f"[+] Filtered {filtered} times! That is {round(filtered * 100 / len(sourceList))}%!")
	print("[+] Filters stopped!")
	return datesList
