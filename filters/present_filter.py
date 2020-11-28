import re
from .utils import (greenPrint, redPrint)
from typing import Final

PRESENT: Final = ["сейчас", "сегод", "в настоящий момент"]

def presentFilter(sourceStr, dateObj):
	for regex in PRESENT:
		found = re.search(regex, sourceStr)
		if found:
			greenPrint(f"PresentFilter -> {sourceStr}")
			dateObj.lock()
