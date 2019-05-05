import search
import google_search
from tweet import Tweet
import yaml
import sys
import glob
import os
from pdb import set_trace
from detail import Detail
from retty import Retty
import pysnooper

def saveImages(url_list, path):

    return 'success'

def getTabelogUrl(num):

    # 検索キーワード
    t = Tweet(num)
    target_keyword = f'{t.name} 食べログ'

    # 検索
    res = search.getSearchResponse(target_keyword)

    # # レスポンスを格納
    # f = open(f"post_tweets/{num}/search_tabelog.yml", "w")
    # f.write(yaml.dump(res, allow_unicode=True))

    print(res['response'][0]['items'][0]['link'])

    # urlをupdate
    t.url = res['response'][0]['items'][0]['link']
    t.save()
    return t.url

def getRelatedImg(num):

    # 検索キーワード
    t = Tweet(num)
    target_keyword = f'{t.name} カフェ 店'
    path = f'post_tweets/{num}/shop'

    # set_trace()

    google_search.main(target_keyword, 20, path, prefix='shop')
    target_keyword = f'{t.name} カフェ food'
    path = f'post_tweets/{num}/food'
    google_search.main(target_keyword, 20, path, prefix='food')
    return 'success'

def getDetails(num):

    # 検索キーワード
    t = Tweet(num)
    d = Detail(f'{t.name}')
    # t.details = d.best()
    # t.save()
    d.simple_export(f'post_tweets/{t.no}/details.txt')
    return 'success'

def createTweet(name):
    list = glob.glob("post_tweets/*")
    num = len(list) + 1
    # print(f'tweet number is {num}')
    t = Tweet(num)
    t.name = name
    t.save()
    return num

@pysnooper.snoop()
def createTweet2(i):
    # list = glob.glob("post_tweets/*")
    # num = len(list)
    num = 83
    # print(1)
    retty = Retty(i)
    # print(2)
    cafes = retty.search()
    # print(3)
    # set_trace()
    print(cafes)
    for cafe in cafes:
    # print(cafes[0])
    # cafe = cafes[0]
        # cafe = {'name':'hoge', 'details': 'fuga'}
        # set_trace()
        num += 1
        if num == 84: continue
        t = Tweet(num)
        t.name = cafe['name']
        t.details = cafe['details']
        t.save()
        getTabelogUrl(num)
        getRelatedImg(num)
        getDetails(num)
    return 'success'



if __name__ == '__main__':
    createTweet2(3)
    # if len(sys.argv) == 2:
    #     i = int(sys.argv[1])
    #     getTabelogUrl(i)
    #     getRelatedImg(i)
    #     getDetails(i)
    # else:
    #     with open('name.txt') as f:
    #         for line in f:
    #             i = createTweet(line.rstrip())
    #             getTabelogUrl(i)
    #             getRelatedImg(i)
    #             getDetails(i)
