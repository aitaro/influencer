import glob
import sys
import os
import yaml
import unicodedata
from tweet import Tweet

num1 = int(sys.argv[1])
if len(sys.argv) == 3:
    num2 = int(sys.argv[2])
else:
    num2 = num1

for i in range(num1, num2+1):
    t = Tweet(i)
    print('-------------------')
    print('No. ' + str(t.no))
    print(t.details)
