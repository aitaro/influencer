import tweepy
import config

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)

auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

tweepyapi = tweepy.API(auth)
tweet_data = tweepyapi.search(q='SCOPP CAFE', count=100)
for tweet in tweet_data:
        print(tweet.text)
        print('************************************************\n')
