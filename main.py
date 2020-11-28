from Date import *
from csv_work.csv_read_write import (getSourceList, writeOutputResult)
from filters.filter_main import mainFilters

def createDateObjectsList(length):
	return [Date() for _ in range(length)]

def main():
	sourceList = getSourceList()
	datesList = createDateObjectsList(len(sourceList))

	mainFilters(sourceList, datesList)

	writeOutputResult(sourceList, datesList)

def test():
	date = Date()
	print(date)

if __name__ == "__main__":
	print("Start:")

	main()
	# test()