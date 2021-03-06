# coding: utf-8
import config
import tweepy
import yaml
from pdb import set_trace
import os
import random
from logger import logger
from slack import slack_notify
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

import sys
sys.stdout = open('log/stdout.log', 'a')
sys.stderr = open('log/stderr.log', 'a+')

from datetime import datetime
print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

print('hello main python start')

tweepyapi = tweepy.API(auth)

def tweet(num):
    tweet_data_path = f'post_tweets/{num}'
    # import text
    f = open(tweet_data_path + "/tweet.yml", "r+")
    tweet_data = yaml.load(f, Loader=yaml.FullLoader)
    filenames = []
    for i in range(4):
        filenames.append(f'{tweet_data_path}/pic{i+1}.jpg')

    media_ids = []
    for filename in filenames:
         res = tweepyapi.media_upload(filename)
         media_ids.append(res.media_id)

    res = tweepyapi.update_status(status=f"{tweet_data['name']}\n\n{tweet_data['content']['details']}\n\n{tweet_data['content']['url']}", media_ids=media_ids)
    set_tweet_id(num, res.id)
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

def set_tweet_id(num, id):
    tweet_data_path = f'post_tweets/{num}'
    f = open(tweet_data_path + "/tweet.yml", "r")
    d = yaml.load(f, Loader=yaml.FullLoader)
    with open(tweet_data_path + "/tweet.yml", "w") as wf:
        d['id'] = id
        yaml.dump(d, wf, allow_unicode=True)

def delete_tweet(num):
    tweet_data_path = f'post_tweets/{num}'
    f = open(tweet_data_path + "/tweet.yml", "r")
    d = yaml.load(f, Loader=yaml.FullLoader)
    id = d.get('id')
    if id: tweepyapi.destroy_status(id)
    d.pop('id')
    with open(tweet_data_path + "/tweet.yml", "w") as wf:
        yaml.dump(d, wf, allow_unicode=True)
    return 'success'

def can_tweet(num):
    return os.path.exists(f'post_tweets/{num}/tweet.yml')

if __name__ == '__main__':
    # print(search())
    try:
        current_no = get_current_no()
        if can_tweet(current_no+1):
            current_no += 1
            print(tweet(current_no))
            set_current_no(current_no)
        else:
            tweet_again_no = random.randint(1,current_no-5)
            delete_tweet(tweet_again_no)
            print(tweet(tweet_again_no))
    except Exception as e:
        logger.error(e)
        slack_notify(str(e.args))

print('hello main python finished')
