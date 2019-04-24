import glob
import sys
import os
from tweet import Tweet

# name = sys.argv[1]
# detail = sys.argv[2]
list = glob.glob("post_tweets/*")
num = len(list) + 1
print(f'tweet number is {num}')
t = Tweet(num)
t.name = 'name'
t.details = 'details'
t.save()
print('success')
