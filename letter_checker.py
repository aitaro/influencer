#coding:utf-8
import glob
import yaml
import unicodedata

if __name__ == '__main__':

  file_list = sorted(glob.glob('post_tweets/*/tweet.yml'))

  for filename in file_list:
      f = open(filename, 'r')
      data = yaml.load(f)
      if unicodedata.east_asian_width((data['name'] + data['content']['details'] + data['content']['url']).encode('unicode')) > 275:
          print(filename)
          print('toolong')
          print(unicodedata.east_asian_width(data['name'] + data['content']['details'] + data['content']['url']).encode('unicode'))
