import glob
import sys
import os

num = int(sys.argv[1])
list = glob.glob(f"post_tweets/{num}/*.jpg") + glob.glob(f"post_tweets/{num}/*.jpeg")
print(f'写真の総数は{len(list)}です')
i = 1
for path in list:
    os.rename(path, f"post_tweets/{num}/pic{i}.jpg")
    i += 1

print('finished')
