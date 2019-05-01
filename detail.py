import urllib
import yaml
from google_search import Google
from bs4 import BeautifulSoup
from pdb import set_trace
from tweet import Tweet
import sys


class Detail:
    def __init__(self, word, c_num=30):
        self.word = word
        self.c_num = c_num

    def search(self):
        google = Google()
        query = google.query_gen(self.word + ' -Retty -食べログ', 'text')
        self.urls = google.url_search(query, self.c_num)

    def createCanditates(self):
        total = 0
        self.candidates = []
        for url in self.urls:

            # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
            req = urllib.request.Request(url)
            try:
                response = urllib.request.urlopen(req)
            except Exception as e:
                print(e)
                print('could not find detail')
                continue
            html = response.read()

            soup = BeautifulSoup(html, "html.parser")


            try:
                cand = {'text': soup.select('meta[name="description"]')[0]['content']}
                self.candidates.append(cand)
            except:
                print('no datails')
            total += 1
            print(f'searched webpage {total}')


    def scoring(self):
        for i, hash in enumerate(self.candidates):
            # set_trace()
            self.candidates[i] = {'text': hash['text'], 'score': self.score(hash['text'])}

    def score(self, text):
        f = open("score_sheet.yml", "r+")
        score_sheet = yaml.load(f, Loader=yaml.FullLoader)
        sum = 0

        if len(text) < 40:
            sum -= 3
        if not type(text) is str:
            return -1000

        for k, v in score_sheet.items():
            if k in text:
                sum += v
        return sum

    def best(self):
        self.search()
        self.createCanditates()
        self.scoring()

        maxScore = 0
        maxDetail = ''
        for cand in self.candidates:
            if maxScore < cand['score']:
                maxScore = cand['score']
                maxDetail = cand['text']
        return maxDetail

    def export(self):
        f = open("details_example.yml", "w+")
        f.write(yaml.dump(self.candidates, allow_unicode=True))

    def list(self):
        self.search()
        self.createCanditates()
        self.scoring()
        # return sorted(self.candidates, key=lambda x: x['score'])
        return map(lambda x: x['text'], sorted(self.candidates, key=lambda x: -x['score']))

    def simple_export(self, path):
        str_ = '\n'.join(self.list())
        with open(path, 'wt') as f:
            f.write(str_)

if __name__ == '__main__':
    t = Tweet(int(sys.argv[1]))
    d = Detail(t.name)
    print(d.best())
    print(d.list())
    d.export()
