import yaml
import os.path
import sys
import unicodedata
from pdb import set_trace

sys.setrecursionlimit(10000)

def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count


class Tweet:

    def __init__(self, num):
        path = f"post_tweets/{num}/tweet.yml"
        self.path = f"post_tweets/{num}"
        if os.path.exists(path):
            f = open(path, "r+")
            twitter_data = yaml.load(f, Loader=yaml.FullLoader)
            self.no = num
            self.name = twitter_data.get('name')
            content = twitter_data.get('content')
            if content:
                self.details = content.get('details')
                self.url = content.get('url')
            else:
                self.details = None
                self.url = None
            self.id = twitter_data.get('id')
        else:
            self.no = num
            self.name = None
            self.details = None
            self.url = None
            self.id = None

    def mkdir(self):
        if not os.path.isdir(self.path):
            os.makedirs(self.path)

    def save(self):
        num = self.no
        twitter_data = {}
        if self.name: twitter_data['name'] = self.name
        twitter_data['content'] = {}
        if self.details: twitter_data['content']['details'] = self.details
        if self.url: twitter_data['content']['url'] = self.url
        if self.id: twitter_data['id'] = self.id
        tweet_data_path = f'post_tweets/{num}'
        self.mkdir()
        # f = open(f"post_tweets/{num}/tweet.yml", "w")
        # f.write(yaml.dump(twitter_data, allow_unicode=True))

        with open(f"post_tweets/{num}/tweet.yml", "w") as wf:
            yaml.dump(twitter_data, wf, allow_unicode=True)

        return 'success'


    def letterChecker(self):
        return get_east_asian_width_count((self.name + self.details + self.url)) > 300

    def reduceDetails(self):
        # set_trace()
        self.details = '。'.join(self.details.split('。')[:-1])

if __name__ == '__main__':
    t = Tweet(1)
    print(t.name)
    t.url = 'http'
    t.save()
