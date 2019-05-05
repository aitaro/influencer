import glob
import sys
import os
import yaml
import unicodedata
from tweet import Tweet


def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

num1 = int(sys.argv[1])
if len(sys.argv) == 3:
    num2 = int(sys.argv[2])
else:
    num2 = num1

for i in range(num1, num2+1):

    # 詳細
    # filename = f'post_tweets/{f}/tweet.yml'
    # f = open(filename, 'r')
    # data = yaml.load(f)
    # if get_east_asian_width_count((data['name'] + data['content']['details'] + data['content']['url'])) > 300:
    #     t = Tweet(i)
    #     d = t.details
    t = Tweet(i)
    print(t.details)
    while t.letterChecker():
        print(t.details)
        t.reduceDetails()
    t.save()




print('finished')
