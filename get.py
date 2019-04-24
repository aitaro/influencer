import search
import google_search
from tweet import Tweet
import yaml
import sys
from pdb import set_trace

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
    target_keyword = f'{t.name} 店'
    path = f'post_tweets/{num}/shop'

    # set_trace()

    google_search.main(target_keyword, 20, path)
    target_keyword = f'{t.name} food'
    path = f'post_tweets/{num}/food'
    google_search.main(target_keyword, 20, path)
    return 'success'

if __name__ == '__main__':
    num1 = int(sys.argv[1])
    if len(sys.argv) == 3:
        num2 = int(sys.argv[2])
    else:
        num2 = num1
    for i in range(num1, num2+1):
        getTabelogUrl(i)
        getRelatedImg(i)
