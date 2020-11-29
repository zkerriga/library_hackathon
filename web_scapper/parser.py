import typing
from bs4 import BeautifulSoup
import requests as rq
from typing import List,Dict
import csv


def request_url(url):
    """
    function return encode data from get(url)
    """
    get_info = rq.get(url)
    get_info.encoding = 'utf-8'
    return get_info

#kill i don't know... maybe it will usefull
def ceate_soup(url):
    """
    function create a soup object
    """
    page = request_url(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup


def find_in_soup_obj(soup, tag, class_=''):
    """
    function take all tags with class from soup
    """
    return soup.find_all(tag, class_=class_)


#create article list
def get_links_articles(lst_links:List[str]):
    res = []
    for link in lst_links:
        link = str(link)
        link = link[link.find('href') + 6 : link.find('.html') + 5]
        link = f'https://storage.rusneb.ru/newspapers/ocr2/{link}'
        res += [link]
    return res

def get_texts_from_url(link:str):
    parser_page_soup = ceate_soup(link)
    txt = ''.join([text.text for text in parser_page_soup.find_all('span')])
    return txt


def find_times_from_csv(csv_file:str, out_list:List[str] = []):
    with open(csv_file, 'r') as csv_f:
        reader = csv.reader(csv_f)
        for row in reader:
            out_list += row
    return out_list[1:]


if __name__ == '__main__':

    out_list = find_times_from_csv('../temporal-thesaurus-analytical-corpora-test.csv', [])

    URLL = 'https://storage.rusneb.ru/newspapers/ocr2/index.html'
    
    Soup = ceate_soup(URLL) #варим суп
    
    lis_links = find_in_soup_obj(Soup, 'div', 'thumbnail') #ищем нужное в супе
    
    only_articles = get_links_articles(lis_links) #get only links from html
    
    text = get_texts_from_url(only_articles[0])

    



    