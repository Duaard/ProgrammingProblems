#!/bin/python3

import os


def gridSearch(G, P):
    # Loop through every char in G
    for row in range(len(G)):
        for col in range(len(G[row])):
            # Check if there's a first match for the pattern
            # And the index is within range
            if G[row][col] == P[0][0] and (row + len(P) <= len(G) and col + len(P[0]) <= len(G[row])):
                # Check is used for breaking loops
                check = True
                # Counter is used to check if all char of P are found
                counter = len(P) * len(P[0])

                # Get the pattern until it breaks
                for p_row in range(len(P)):
                    for p_col in range(len(P[p_row])):
                        if P[p_row][p_col] != G[row + p_row][col + p_col]:
                            # Pattern checking not complete, break the loops
                            check = False
                            break
                        else:
                            # Deduct this match to the counter
                            counter -= 1
                            if counter == 0:
                                return 'YES'

                    # Break the loop for the row
                    if not check:
                        break

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
