import re
import datetime
from typing import Final
from .utils import (greenPrint, redPrint)

def getNbrYearQuarter(sourceStr: str):
	match: list = sourceStr.split('квартал')
	if len(match) == 1:
		return 0, 0
	nbr_quarter: list = re.findall(r'\d+', match[0])
	year_quarter: list = re.findall(r'\d+', match[1])
	quarter: int = 0
	year: int = 0
	if nbr_quarter:
		quarter = int(nbr_quarter[0])
		if quarter > 4 or quarter < 1:
			quarter = 0
	if year_quarter:
		year = int(year_quarter[0])
	return quarter, year

def getQuarter(sourceStr: str):
	"""
	Integers in l_quarters is nbr of months
	"""
	quarter, year = getNbrYearQuarter(sourceStr)
	if quarter == 0:
		return None
	greenPrint("Quarter " + sourceStr)
	return quarter, year
#
# l = [
# 		"1 квартал 2020 г.",
# 		 "квартал",
# 		"3 кварталы",
# 		"1 квартал",
# 		"1 квартал 2020-го",
# 		"2 квартал 2018 года",
# 		"в течение 2 квартала 2018 года",
# 		"2 квартал 2018 года",
# 		"на протяжении 2 квартала 2018 года",
# 		"квартал",
# 		"квартет",
# 		"кварки",
# 		"1 квартал 2020 г.",
# ]
#
#
#
#
# if __name__ == "__main__":
# 	for i in l:
# 		quarter: tuple = getQuarter(i)
# 		print(f"{i}-{quarter} !")
#
