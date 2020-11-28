import re
from typing import Final
from .ru_number_to_str import replaceRuNumberToStr

REPLACE_PAIRS: Final = [
	("ё", "е"),

	("янв.", "январь"),
	# ("", "февраль"),
	# ("", "март"),
	("апр.", "апрель"),
	# ("", "май"),
	# ("", "июнь"),
	# ("", "июль"),
	("авг.", "август"),
	# ("", "сентябрь"),
	("окт.", "октябрь"),
	# ("", "ноябрь"),
	("дек.", "декабрь"),

	("пн.", "понедельник"),
	("вт.", "вторник"),
	("ср.", "среда"),
	("чт.", "четверг"),
	("пт.", "пятница"),
	("сб.", "суббота"),
	("вс.", "воскресенье"),

	("(", ""),
	(")", ""),
]

# 24-го 5-й 31-e
DATE_FORMS_REGEX: Final = r"(\d{1,2})([-]{0,1}[а-я]{1,2})"

def textFilter(sourceStr: str):
	newStr = sourceStr.lower()

	for case in REPLACE_PAIRS:
		newStr = newStr.replace(case[0], case[1])

	found = re.search(DATE_FORMS_REGEX, newStr)
	if found:
		newStr = newStr.replace(found[0], found[1])
	newStr = replaceRuNumberToStr(newStr)
	return newStr
