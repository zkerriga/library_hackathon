import csv
from Date import *

def getSourceList():
	with open("temporal-thesaurus-analytical-corpora-test.csv", 'r') as file:
		sourceList = list(csv.reader(file))
	return sourceList

def writeOutputResult(sourceList, datesList):
	result = "result.csv"
	with open(result, 'w') as file:
		writer = csv.writer(file, delimiter=',')
		for i in range(len(sourceList)):
			writer.writerow(",".join([sourceList[i], datesList[i]]))

def createDateObjectsList(length):
	return [Date() for _ in range(length)]

def main():
	sourceList = getSourceList()
	datesList = createDateObjectsList(len(sourceList))
	writeOutputResult(sourceList, datesList)

def test():
	date = Date()
	print(date)

if __name__ == "__main__":
	print("Start:")

	main()
	# test()