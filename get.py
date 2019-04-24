import search
from tweet import Tweet
import yaml

def get_tabelog_url(num):

    # 検索キーワード
    t = Tweet(num)
    target_keyword = f'{t.name} 食べログ'

    # 検索
    res = search.getSearchResponse(target_keyword)
    # レスポンスを格納

    f = open(f"post_tweets/{num}/search_tabelog.yml", "w")
    f.write(yaml.dump(res, allow_unicode=True))

    print(res['response'][0]['items'][0]['link'])

    t.url = res['response'][0]['items'][0]['link']
    t.save()
    return t.url


if __name__ == '__main__':

    get_tabelog_url(15)
    get_tabelog_url(16)
    get_tabelog_url(17)
