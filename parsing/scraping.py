import requests
from bs4 import BeautifulSoup
from parsing.create_bs import headers, url


def get_href():
    req = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(req.text, 'lxml')
    href_author = []
    table_author = bs.find('div', class_='lt-body bg-transparent bold').find_all('div',
                                                                                 class_='defs-lt-gallery pointer float-left w-p*20 h-p*30')
    for t in table_author:
        href_author.append(url + t.find_next('a')['href'])
    return href_author
