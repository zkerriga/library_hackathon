import csv
from Date import *

def main():
	print("Start:")
	text = ""

	with open("temporal-thesaurus-analytical-corpora-test.csv", 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			text += row[0] + ' ; '

def test():
	date = Date()
	print(date)

if __name__ == "__main__":
	# main()
	test()