#!/bin/python3

import os


def weightedUniformStrings(s, queries):

    # Add the weight of each c in s
    # Use a dict for O(1) search
    w = {}

    count = 1
    prev = ''
    for c in s:
        if c == prev:
            count += 1
        else:
            count = 1

        # Handle populating of value
        val = (ord(c) - 96) * count
        ch = c * count
        w[val] = ch

        prev = c

    ans = []
    for q in queries:
        if q in w:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
 #!/bin/python3


def weightedUniformStrings(s, queries):

    # Add the weight of each c in s
    # Use a dict for O(1) search
    w = {}

    count = 1
    prev = ''
    for c in s:
        if c == prev:
            count += 1
        else:
            count = 1

        # Handle populating of value
        val = (ord(c) - 96) * count
        w[val] = 1

        prev = c

    ans = []
    for q in queries:
        if q in w:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
