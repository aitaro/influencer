import yaml


tweet_data_path = f'post_tweets/{1}'
# import text
f = open(tweet_data_path + "/tweet.yml", "r")
d = yaml.load(f, Loader=yaml.FullLoader)
with open(tweet_data_path + "/tweet.yml", "w") as wf:
    d['test'] = 'hoge'
    yaml.dump(d, wf, allow_unicode=True)
