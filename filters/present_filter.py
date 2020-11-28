import re

PRESENT = ["сейчас", "сегод", "в настоящий момент"]

def presentFilter(sourceStr, dateObj):
	found = None

	for regex in PRESENT:
		found = re.search(regex, sourceStr)
		if found:
			print(f"[+] PresentFilter -> {sourceStr}")
			dateObj.lock()