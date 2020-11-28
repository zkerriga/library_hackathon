# import Date
import csv
from natasha import (
	Segmenter,
	MorphVocab,
	
	NewsEmbedding,
	NewsMorphTagger,
	NewsSyntaxParser,
	NewsNERTagger,
	
	PER,
	NamesExtractor,
	DatesExtractor,
	MoneyExtractor,
	AddrExtractor,

	Doc
)

def main():
	print("Start:")
	text:str = ""

	with open("temporal-thesaurus-analytical-corpora-test.csv", 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			text += row[0] + ' ; '

	segmenter = Segmenter()
	morph_vocab = MorphVocab()

	emb = NewsEmbedding()
	morph_tagger = NewsMorphTagger(emb)
	syntax_parser = NewsSyntaxParser(emb)
	ner_tagger = NewsNERTagger(emb)

	names_extractor = NamesExtractor(morph_vocab)
	dates_extractor = DatesExtractor(morph_vocab)
	money_extractor = MoneyExtractor(morph_vocab)
	addr_extractor = AddrExtractor(morph_vocab)
	
	# doc = Doc(text)
	# doc.segment(segmenter)
	# print(doc)
	# print(doc.sents[:2])
	# print(doc.tokens[:5])

	listDates = list(dates_extractor(text))
	with open("result.csv", 'w') as fileOut:
		for el in listDates:
			fileOut.write(str(el) + "\n")

main()