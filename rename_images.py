import glob
import sys
import os

num1 = int(sys.argv[1])
if len(sys.argv) == 3:
    num2 = int(sys.argv[2])
else:
    num2 = num1
for i in range(num1, num2+1):

    # 写真
    print(f'tweet: {i}')
    list = glob.glob(f"post_tweets/{i}/*.jpg") + glob.glob(f"post_tweets/{i}/*.jpeg")
    print(f'写真の総数は{len(list)}です')
    j = 1
    for path in list:
        os.rename(path, f"post_tweets/{i}/pic{j}.jpg")
        j += 1

    # 詳細
    

print('finished')
