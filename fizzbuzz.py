
import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for i in range(1, n+1):
        mod_3 = i % 3
        mod_5 = i % 5
        if mod_3 == 0 and mod_5 == 0:
            print("FizzBuzz")
        elif mod_3 == 0 and mod_5 != 0:
            print("Fizz")
        elif mod_3 != 0 and mod_5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
