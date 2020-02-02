#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mi, ma = arr[0], arr[0]

    for i in arr:
        if i > ma:
            ma = i
        if i < mi:
            mi = i
    
    n_mi, n_ma = arr.count(mi), arr.count(ma)
    s_mi, s_ma = 0,0
    for i in arr:
        if i != ma:
            s_mi += i
        if i != mi:
            s_ma += i
    s_mi += ma * (n_ma - 1)
    s_ma += mi * (n_mi - 1)

    print("{} {}".format(s_mi, s_ma))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
