def nth_largest(arr, k):
    sorted_arr = sorted(arr, reverse= 1)
    return sorted_arr[k - 1]
print(nth_largest([3, 2, 1, 5, 6, 4], 6))