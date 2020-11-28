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

	("ровно", ""),
]

# 24-го 5-й 31-e
NUMBER_WITH_HYPHEN: Final = r"(\d{1,2})([-]{0,1}[а-я]{1,2})"
# день тому назад
AGO_CLEAR: Final = r"(тому)( назад)"

def simpleReplaces(newStr: str):
	for case in REPLACE_PAIRS:
		newStr = newStr.replace(case[0], case[1])
	return newStr

def clearNumbersWithHyphen(newStr: str):
	found = re.search(NUMBER_WITH_HYPHEN, newStr)
	if found:
		newStr = newStr.replace(found[0], found[1])
	found = re.search(AGO_CLEAR, newStr)
	if found:
		newStr = newStr.replace(found[0], found[2])
	return newStr

def textFilter(sourceStr: str):
	newStr = sourceStr.lower()
	newStr = simpleReplaces(newStr)
	newStr = clearNumbersWithHyphen(newStr)
	newStr = replaceRuNumberToStr(newStr)
	return newStr
