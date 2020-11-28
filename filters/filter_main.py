from .present_filter import presentFilter
from .dateparser_filter import *
from .utils import (green, red)

def mainFilters(sourceList, datesList):
	print("[+] Filters started!")
	filtered: int = 0

	for sourceStr, dateObj in zip(sourceList, datesList):
		dateParserFilter(sourceStr, dateObj)
		if not dateObj.isLocked():
			presentFilter(sourceStr, dateObj)

		if dateObj.isLocked():
			filtered += 1
		else:
			red(sourceStr)

	print(f"[+] Filtered {filtered} times!")
	print("[+] Filters stopped!")
