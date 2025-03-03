def max_element(arr):
    sorted_array = sorted(arr, reverse= 1)
    return sorted_array[0]
print(max_element([1,2,3,4,5,6,7,8,33,1,22,45,6,9,10]))