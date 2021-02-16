import math
import os
import random
import re
import sys
from collections import Counter
import math

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    myDict = {i:ar.count(i) for i in ar}
    for value in myDict.values():
       if value/2 > 0.5:
           count = count + math.floor(value/2)
    print (count)       




ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
sockMerchant(n,ar)


    

