

def insertion_sort(l):
    # Loop through the array starting from index 1
    for i in range(1, len(l)):
        # 4 1 3 5 6 2
        # Assign the prev element as j
        j = i-1
        # Assign the current element as key
        key = l[i]
        # Loop while j is within index range and prev element is greater than current
        while (j >= 0) and (l[j] > key):
            # Move the prev element to current index
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str, ar)))
