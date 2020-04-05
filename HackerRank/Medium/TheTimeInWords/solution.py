#!/bin/python3

import os

time_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    40: 'forty',
    50: 'fifty'
}


def timeInWords(h, m):
    minutes = ''
    adjective = ''

    # Set the adjective to be used based on minutes
    if m >= 1 and m <= 30:
        # Use past
        adjective = 'past'
    elif m != 0:
        # Use to
        adjective = 'to'
        # Use the next hour to reference time
        h += 1

    # If the time is more than 30, invert it
    if m > 30:
        m = 60 - m

    # Get the minutes to be used
    if m == 0:
        # Return the hour with o' clock
        return time_dict[h] + " o' clock"
    elif m == 15 or m == 45:
        # Use quarter
        minutes = 'quarter'
    elif m == 30:
        # Use half
        minutes = 'half'
    else:
        # Convert the minutes into words
        if m < 20:
            # Simply get the conversion
            minutes = time_dict[m]
        else:
            # Build the words

            tens = m // 10 * 10
            ones = m % 10
            minutes = time_dict[tens] + ' ' + time_dict[ones]
        if m > 1:
            minutes += ' minutes'
        else:
            minutes += ' minute'

    # Combine everything and return
    return minutes + ' ' + adjective + ' ' + time_dict[h]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
