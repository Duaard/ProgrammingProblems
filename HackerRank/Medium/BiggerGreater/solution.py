#!/bin/python3

import os


def biggerIsGreater(w):
    # Available letters
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # Keep track of the heirarchy of letters
    char_dict = {}
    # Save the index of each letter
    for index, letter in enumerate(alpha):
        char_dict[letter] = index

    # Temporarily convert w to a list
    orig = list(w)
    w = list(w)

    # Keep track of available chars
    char_list = [0] * len(alpha)
    index = None

    # Loop through each place starting from the last element
    for i in range(len(w) - 1, -1, -1):
        # Get the index of this letter
        alpha_index = char_dict[w[i]]
        if i != len(w) - 1:
            e = w[i]
            e_index = 0
            # Get the least possible index for this position
            for j in range(alpha_index + 1, len(alpha)):
                # Check if there's an available character
                if char_list[j] > 0:
                    e_index = j
                    e = alpha[e_index]
                    break

            # Check if e was changed
            if e > w[i]:
                # Break the loop and re-construct the word using the remaining char_list
                index = i + 1
                # Add this element to char_list
                char_list[alpha_index] += 1
                w[i] = e
                # Remove e from char list
                char_list[e_index] -= 1
                break

        char_list[alpha_index] += 1

    #  Check if the index was changed
    if index != None:
        # Add the remaining char from least to greatest
        place = 0
        for i in range(len(alpha)):
            for j in range(char_list[i]):
                w[index + place] = alpha[i]
                place += 1

    if orig == w:
        return 'no answer'
    return "".join(w)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
