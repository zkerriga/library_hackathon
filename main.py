from Date import *
from csv_work.csv_read_write import (getSourceList, writeOutputResult)
from filters.filter_main import mainFilters
from typing import Final

def createDateObjectsList(length):
	return [Date() for _ in range(length)]

def main():
	sourceList: Final = getSourceList()

	copySourceList = sourceList.copy()
	datesList = createDateObjectsList(len(copySourceList))

	mainFilters(copySourceList, datesList)

	writeOutputResult(sourceList, datesList)

def test():
	pass

if __name__ == "__main__":
	print("Start:")

	main()
	test()
