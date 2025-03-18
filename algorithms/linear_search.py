def linear_search(arr, target):
    for i in range(len(arr)):   # O(n)
        if arr[i] == target:    # O(1)
            return i            # O(1)
    return -1                   # O(1)
