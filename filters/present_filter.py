import re
from .utils import (green, red)

PRESENT = ["сейчас", "сегод", "в настоящий момент"]

def presentFilter(sourceStr, dateObj):
	found = None

	for regex in PRESENT:
		found = re.search(regex, sourceStr)
		if found:
			green(f"PresentFilter -> {sourceStr}")
			dateObj.lock()
