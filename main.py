import csv
from Date import *

def getSourceList():
	with open("temporal-thesaurus-analytical-corpora-test.csv", 'r') as file:
		reader = csv.reader(file)
	return reader

def createDateObjectsList(length):
	return [Date() for _ in range(length)]

def main():
	sourceList = getSourceList()
	datesList = createDateObjectsList(len(sourceList))

def test():
	date = Date()
	print(date)

if __name__ == "__main__":
	print("Start:")

	main()
	test()