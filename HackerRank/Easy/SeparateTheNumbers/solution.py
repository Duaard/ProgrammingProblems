#!/bin/python3


def separateNumbers(s):

    # The smallest init value possible
    init_val = 0
    # How many places the current num has
    n = 1
    n_next = 1
    # Identifies if s is beautiful
    b = False

    # Loop through each possible initial value in s
    i = 0
    inc = 1
    while i < len(s):
        if i == 0:
            # Set initial value
            init_val = int(s[i:i+n])
            next_val = str(init_val + 1)
            n_next = len(next_val)
        else:
            if s[i:i+n_next] == next_val:
                # This is beatiful
                next_val = str(int(s[i:i+n_next]) + 1)
                inc = len(s[i:i+n_next])
                n_next = len(next_val)
                b = True

            else:
                # Adjust n and reset i
                n += 1
                inc = n
                i = 0
                b = False
                continue

        # Increment i
        i += inc
    if b:
        print(f'YES {init_val}')
    else:
        print('NO')


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
