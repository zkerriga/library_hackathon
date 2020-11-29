from Date import *
from csv_work.csv_read_write import (getSourceList, writeOutputResult)
from filters.filter_main import mainFilters
from typing import Final
from parser import only_articles, get_texts_from_url
import json

TEN_ARTICLES = only_articles[:11]

def create_json(out_file:str):
	src_list = getSourceList()
	dates_list = createDateObjectsList(len(src_list))
	mainFilters(src_list.copy(), dates_list)
	for i in range(len(TEN_ARTICLES)):
		data = {'link':'', 'case': [], 'convert_case': []}
		text = get_texts_from_url(TEN_ARTICLES[i])
		for j in range(len(src_list)):
			if src_list[j] in text:
				data['case'] += [src_list[j]]
				data['convert_case'] += [str(dates_list[j])]
		data['link'] = TEN_ARTICLES[i]
		with open(out_file, 'a') as ouf:
			json.dump(data, ouf, sort_keys = False, indent = 4, ensure_ascii = False)
			ouf.write(', ')
	return f'Was write elements in {out_file}'


def createDateObjectsList(length):
	return [Date() for _ in range(length)]

def main():
	sourceList: Final = getSourceList()

	copySourceList = sourceList.copy()
	datesList = createDateObjectsList(len(copySourceList))

	mainFilters(copySourceList, datesList)

	writeOutputResult(sourceList, datesList)

def test():
	mainFilters(["сегодня"], [Date()])

if __name__ == "__main__":
	print("Start:")
	
	print(create_json('output.json'))
	# test()
