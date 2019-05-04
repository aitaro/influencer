import json
import os
import sys
import urllib

from bs4 import BeautifulSoup
import requests
from pdb import set_trace


class Google:
    def __init__(self):
        self.GOOGLE_SEARCH_URL = 'https://www.google.co.jp/search'
        self.session = requests.session()
        self.session.headers.update(
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'})

    def search(self, keyword, maximum):
        print('begin searching', keyword)
        query = self.query_gen(keyword, 'image')
        return self.image_search(query, maximum)

    def query_gen(self, keyword,type):
        # search query generator
        page = 0
        while True:
            query = {
                'q': keyword,
                'ijn': str(page),
                'hl': 'ja',
                'lr': 'lang_ja'
            }
            if type == 'image':
                query['tbm'] = 'isch'

            params = urllib.parse.urlencode(query)

            yield self.GOOGLE_SEARCH_URL + '?' + params
            page += 1

    def url_search(self, query_gen, maximum):
        # search image
        result = []
        total = 0
        while True:
            html = self.session.get(next(query_gen)).text
            soup = BeautifulSoup(html, 'lxml')
            urls = [a['href'] for a in soup.select('.bkWMgd .rc .r > a')]

            # add search result
            if not len(urls):
                print('-> no more urls')
                break
            elif len(urls) > maximum - total:
                result += urls[:maximum - total]
                break
            else:
                result += urls
                total += len(urls)
        return result



    def image_search(self, query_gen, maximum):
        # search image
        result = []
        total = 0
        while True:
            # search
            html = self.session.get(next(query_gen)).text
            soup = BeautifulSoup(html, 'lxml')
            elements = soup.select('.rg_meta.notranslate')
            jsons = [json.loads(e.get_text()) for e in elements]
            imageURLs = [js['ou'] for js in jsons]

            # add search result
            if not len(imageURLs):
                print('-> no more images')
                break
            elif len(imageURLs) > maximum - total:
                result += imageURLs[:maximum - total]
                break
            else:
                result += imageURLs
                total += len(imageURLs)

        print('-> found', str(len(result)), 'images')
        return result

def details(keyword, num):
    google = Google()
    query = google.query_gen(keyword, 'text')
    return google.details_search(google.url_search(query, num))


def main(keyword, num, path, prefix=''):
    google = Google()
    name = keyword
    # data_dir = 'data/'
    os.makedirs(path, exist_ok=True)
    # os.makedirs('data/' + name, exist_ok=True)

    # search image
    result = google.search(
        name, maximum=int(num))

    # download
    download_error = []
    for i in range(len(result)):
        print('-> downloading image', str(i + 1).zfill(4))
        try:
            urllib.request.urlretrieve(
                result[i], path + '/' + prefix + str(i + 1).zfill(4) + '.jpg')
        except Exception as e:
            print(e)
            print('--> could not download image', str(i + 1).zfill(4))
            download_error.append(i + 1)
            continue

    print('complete download')
    print('├─ download', len(result)-len(download_error), 'images')
    print('└─ could not download', len(
        download_error), 'images', download_error)


if __name__ == '__main__':
    # main('猫',10,'g')
    google = Google()
    query = google.query_gen('京都', 'text')
    print(google.url_search(query, 20))
