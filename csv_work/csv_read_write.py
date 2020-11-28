import csv

def getSourceList():
	sourceList = []
	with open("temporal-thesaurus-analytical-corpora-test.csv", 'r') as file:
		reader = csv.reader(file)
		for line in reader:
			sourceList.append(line[0])
	return sourceList[1:]

def writeOutputResult(sourceList, datesList):
	result = "result.csv"
	with open(result, 'w') as file:
		writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
		writer.writerow(["Id", "Expected"])
		for i in range(len(sourceList)):
			writer.writerow([sourceList[i], datesList[i]])
