import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    sea_Level = 0
    myList = [0 for i in range(len(path))]
    mytempList = [0 for i in range(len(path))]
    index = 0
    k = 0
    n = 0
    valley = 0
    for i in path:
        if i == "U":
            myList[index] = 1
        else:
            myList[index] = -1
        index = index + 1  
    print (myList) 
    for j in myList:
        sea_Level = sea_Level + j
        mytempList[k] = sea_Level
        k = k + 1
    print (mytempList)
    if myList[0] == -1:
        valley = valley + 1 

    for l in mytempList:
        if n + 2 < steps:
             if mytempList[n] == 0 and mytempList[n+1] == -1:
                valley = valley + 1 
                

       
        n = n + 1    

     
    print (valley)



steps = 12
path = ["D","D","U","U","D","D","U","D","U","U","U","D"]
countingValleys(steps,path)