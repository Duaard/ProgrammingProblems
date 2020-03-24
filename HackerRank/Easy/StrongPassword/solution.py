#!/bin/python3

import os


def elementPresent(password, db_string):
    # Return wether list a and b have a common element

    # Make the lists argument set
    return set(password) & set(db_string)


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    # These are the requirements for a strong password
    requirements = ["0123456789", "abcdefghijklmnopqrstuvwxyz",
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "!@#$%^&*()-+"]

    # Check how many requirements needs to be satisfied
    counter = 0
    for req in requirements:
        if not elementPresent(password, req):
            counter += 1

    # Check if the length doesn't reach the requirement
    if n + counter < 6:
        counter += 6 - (n + counter)

    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
