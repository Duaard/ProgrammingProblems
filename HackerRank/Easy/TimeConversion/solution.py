#!/bin/python3

import os
import sys

def timeConversion(s):
    am_or_pm = s[len(s)-2:len(s)]
    m_s = s[2:len(s)-2]
    h = s[0:2]
    
    if am_or_pm == 'AM' and s[0:2] == '12':
        h = '00'
    elif am_or_pm == 'PM':
        if h != '12':
            h = int(s[0:2]) + 12
    return str(h) + m_s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
