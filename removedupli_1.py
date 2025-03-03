def remove_duplicants(arr):
    return list(set(arr))
print(*remove_duplicants([1,2,2,3,3,4,5,5,6]))

#O(N)