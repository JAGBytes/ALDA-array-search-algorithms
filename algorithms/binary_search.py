def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # O(1)

    while left <= right:           # O(log n)
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:     # O(1)
            return mid             # O(1)
        elif arr[mid] < target:    # O(1)
            left = mid + 1         # O(1)
        else:
            right = mid - 1        # O(1)
    
    return -1                      # O(1)
