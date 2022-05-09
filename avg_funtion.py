#!/bin/python

import math
import os
import random
import re
import sys


# write your code here
def avg(*nums):
    count = 0
    sum_value = 0
    for i in nums:
        count += 1
        sum_value += i
    avg_value = sum_value/count
    return avg_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = map(int, raw_input().split())
    res = avg(*nums)
    print(res)

    fptr.write('%.2f' % res + '\n')

    fptr.close()
