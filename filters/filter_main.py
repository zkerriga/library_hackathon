from .present_filter import presentFilter

def mainFilters(sourceList, datesList):
	print("[+] Filters started!")

	for sourceStr, dateObj in zip(sourceList, datesList):
		presentFilter(sourceStr, dateObj)

	print("[+] Filters stopped!")
