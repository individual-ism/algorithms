#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    listS = s.split(":")
    if listS[2].__contains__("PM") and int(listS[0]) < 12:
        listS[0] = str(int(listS[0]) + 12)
        listS[2] = listS[2][0:2]
    elif listS[2].__contains__("AM") and listS[0] == "12":
        listS[0] == "00"
        listS[2] = listS[2][0:2]
    else:
        listS[2] = listS[2][0:2]
    strS = ""
    for i in range(0, 3):
        strS += ":".join(listS[i])
    # print(type(strS))
    return strS

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
