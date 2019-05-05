import urllib
import yaml
# from google_search import Google
import requests
from bs4 import BeautifulSoup
from pdb import set_trace
# from tweet import Tweet
# import sys
import sys
sys.setrecursionlimit(10000)

class Retty:
    def __init__(self, page):
        self.page = page
        self.search_url = f'https://retty.me/theme/100014800/?page={page}'

    def search(self):
        html_doc = requests.get(self.search_url).text
        soup = BeautifulSoup(html_doc, 'lxml') # BeautifulSoupの初期化
        shops = soup.select('.mt-restaurant')
        cafes = []
        # set_trace()
        for shop in shops:
            # print(shop.select('.mt-restaurant-title__main-name > a'))
            # print(shop.select('.mt-restaurant-description'))
            if shop.select('.mt-restaurant-description'):
                description = shop.select('.mt-restaurant-description')[0].string
            else:
                description = ''
            title = shop.select('.mt-restaurant-title__main-catchcopy > a')[0].string or ''
            # set_trace()
            cafe = {
                'name': str(shop.select('.mt-restaurant-title__main-name > a')[0].string),
                'details': self.createDetails(title, description)
                }
            cafes.append(cafe)
        return cafes

    def createDetails(self, title, description):
        list = description.split('。')
        # if len(list) == 1:
        #     list.append('')
        # set_trace()
        return str(title + '。'+ '。'.join(list[1:])).replace(' ', '')


if __name__ == '__main__':
    retty = Retty(3)
    print(retty.search())
