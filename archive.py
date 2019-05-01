#coding:utf-8
import glob
import yaml
import shutil
import os


def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

if __name__ == '__main__':

  dir_list = sorted(glob.glob('post_tweets/*'))
  print(dir_list)
  #
  for dirname in dir_list:
      new_dirname = 'archive/' + dirname[12:]
      print(new_dirname)
      if os.path.exists(dirname + '/shop'):
          shutil.move(dirname + '/shop', new_dirname+'/shop')
      if os.path.exists(dirname + '/food'):
          shutil.move(dirname + '/food', new_dirname+'/food')
      # os.makedirs('temp/dir1/dir', exist_ok=True)
      # if get_east_asian_width_count((data['name'] + data['content']['details'] + data['content']['url'])) > 275:
      #     print(filename)
      #     print('too long')
      #     print(get_east_asian_width_count(data['name'] + data['content']['details'] + data['content']['url']))
