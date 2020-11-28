from .present_filter import presentFilter

def mainFilters(sourceList, datesList):
	print("[+] Filters started!")

	for sourceStr, dateObj in zip(sourceList, datesList):
		if not dateObj.isLocked():
			presentFilter(sourceStr, dateObj)

	print("[+] Filters stopped!")
