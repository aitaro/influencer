# coding: utf-8
import config
import tweepy
import yaml
from pdb import set_trace
import os
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

tweepyapi = tweepy.API(auth)

def tweet(num):
    tweet_data_path = f'post_tweets/{num}'
    # import text
    f = open(tweet_data_path + "/text.yml", "r+")
    tweet_data = yaml.load(f, Loader=yaml.FullLoader)
    filenames = []
    for i in range(4):
        filenames.append(f'{tweet_data_path}/pic{i+1}.jpg')

    media_ids = []
    for filename in filenames:
         res = tweepyapi.media_upload(filename)
         media_ids.append(res.media_id)

    tweepyapi.update_status(status=f"{tweet_data['name']}\n\n{tweet_data['details']}\n\n{tweet_data['url']}", media_ids=media_ids)
    return 'success'

def get_current_no():
    f = open("twitter.yml", "r+")
    twitter_data = yaml.load(f, Loader=yaml.FullLoader)
    return twitter_data['current_no']

def set_current_no(current_no):
    f = open("twitter.yml", "r+")
    twitter_data = yaml.load(f, Loader=yaml.FullLoader)
    twitter_data['current_no'] = current_no
    with open("twitter.yml", "w") as wf:
        yaml.dump(twitter_data, wf)
    return 'suceess'

if __name__ == '__main__':
    # print(search())
    current_no = get_current_no()
    current_no += 1
    print(tweet(current_no))
    set_current_no(current_no)
