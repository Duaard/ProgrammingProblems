#!/bin/python3

import os


def caesarCipher(s, k):
    # Create a string representation of the letters
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Loop through each char and convert it using k
    e = ''
    for c in s:
        if c.upper() in letters:
            # Encrypt this letter by converting to ascii
            # and capping values to 26
            v = ((ord(c.upper()) - 65) + k) % 26
            if c.isupper():
                c = letters[v]
            else:
                c = letters[v].lower()
        e += c

    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
