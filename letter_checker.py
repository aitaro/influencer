#coding:utf-8
import glob
import yaml
import unicodedata


def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

if __name__ == '__main__':

  file_list = sorted(glob.glob('post_tweets/*/tweet.yml'))

  for filename in file_list:
      f = open(filename, 'r')
      data = yaml.load(f)
      if get_east_asian_width_count((data['name'] + data['content']['details'] + data['content']['url'])) > 275:
          print(filename)
          print('too long')
          print(get_east_asian_width_count(data['name'] + data['content']['details'] + data['content']['url']))
