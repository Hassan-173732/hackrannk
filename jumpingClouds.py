import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    p = 0

    while p+1 < len(c):

        if c[p+1] == 0:
            if p+2 < len(c) and c[p+2] == 0:
                p += 2
            else:
                p += 1

            jumps += 1

        else:
            while c[p+1] != 0:
                p += 1
            p += 1
            jumps += 1

    return jumps

          
                    


    

    

c = [0,1,1,1,0,0]
print(jumpingOnClouds(c))