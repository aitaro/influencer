import config
import tweepy

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

tweepyapi = tweepy.API(auth)

tweepyapi.update_status('Hello World!2')
print("Hello " + tweepyapi.me().name)
