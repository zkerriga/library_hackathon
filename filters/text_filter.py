import re
from typing import Final
from .ru_number_to_str import replaceRuNumberToStr

REPLACE_PAIRS: Final = [
	("ё", "е"),
	("(", ""),
	(")", ""),
	(" кв. ", " квартал "),
	(" кв ", " квартал "),
	("ровно", ""),
	("за этот", "этот"),
	("весь текущий", "текущий"),
	("уходящий", "этот"),
	("истекающий", "этот"),
	("грядущий", "следующий"),
	("предстоящий", "следующий"),
	("в эту", "в"),
	("в том", "в прошлом"),
	("в ту", "в прошлую"),
	("последний день недели", "воскресенье"),
	("ближайшее", "это"),
	("за эту", "на этой"),
	("всю эту", "на этой"),
	("прошлую", "прошлая"),
	("предыдущая", "прошлая"),
	("предыдущей", "прошлая"),
	("прошедшей", "прошлой"),
	("за прошедшую", "на прошлой"),
	("предстоящая", "следующая"),
	("будущая", "следующая"),
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

# ночью, в 4 часа
NIGHT_REGEX: Final = r"((ночью|утром).*\s)(\d{1,2})(\s*час(а|ов|))"
DAY_REGEX: Final = r"((вечером|днем).*\s)(\d{1,2})(\s*час(а|ов|))"

def partOfDayReplaces(newStr: str):
	found = re.match(NIGHT_REGEX, newStr)
	if found:
		newStr = newStr.replace(found.group(1), "")
		return newStr
	found = re.match(DAY_REGEX, newStr)
	if found:
		newStr = newStr.replace(found.group(1), "")
		hour: int = int(found.group(2))
		if hour < 12:
			newStr = newStr.replace(found.group(2), f"{hour + 12}")
		return newStr
	return newStr

ROMAN: Final = [
	("IV ", "4 "),
	("III ", "3 "),
	("II ", "2 "),
	("I ", "1 "),
]

def toArabicNumbers(newStr: str):
	for fromStr, toStr in ROMAN:
		newStr = newStr.replace(fromStr, toStr)
	return newStr

def textFilter(sourceStr: str):
	newStr: str = toArabicNumbers(sourceStr)
	newStr = newStr.lower()
	newStr = simpleReplaces(newStr)
	newStr = clearNumbersWithHyphen(newStr)
	replaced: str = replaceRuNumberToStr(newStr)
	if replaced:
		newStr = replaced
	newStr = partOfDayReplaces(newStr)
	return newStr
