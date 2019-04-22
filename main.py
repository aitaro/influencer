# coding: utf-8
import config
import tweepy
import yaml
from pdb import set_trace
import os
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

tweepyapi = tweepy.API(auth)

# tweepyapi.update_status('Hello World!2')
# print("Hello " + tweepyapi.me().name)


# searchWord = ["金足農業","応援"]
# print(tweepyapi.search(q=searchWord, lang='ja', result_type='recent', count=5))

# q @squidzer min_retweets:1000
# filter:video min_retweets:1



def search():
    res = tweepyapi.search('どういうテンションやねんwww filter:videos',result_type='resent', count=1)
    print(len(res))
    for tweet in res:
        print(tweet.user.verified)
        if tweet.user.verified:
            continue
        f = open(f"tweets/{tweet.id}.yml", "w+")
        f.write(yaml.dump(tweet._json, allow_unicode=True))
        f.close()

    if len(res) > 0:
        return 'success'
    else:
        return 'failed'

def tweet(num):
    tweet_data_path = f'post_tweets/{num}'
    # import text
    f = open(tweet_data_path + "/text.yml", "r+")
    tweet_data = yaml.load(f, Loader=yaml.FullLoader)
    filenames = []
    for i in range(4):
        filenames.append(f'{tweet_data_path}/pic{i+1}.jpeg')

    media_ids = []
    for filename in filenames:
         res = tweepyapi.media_upload(filename)
         media_ids.append(res.media_id)

    tweepyapi.update_status(status=f"{tweet_data['name']}\n\n{tweet_data['details']}\n\n{tweet_data['url']}", media_ids=media_ids)
    return 'success'


if __name__ == '__main__':
    # print(search())
    print(tweet(1))
