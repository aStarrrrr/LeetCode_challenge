def max_element(arr):
    max_ele = arr[0]
    for data in arr:
        if data > max_ele:
            max_ele = data
    return max_ele
print(max_element([1,2,3,4,5,678,7,8,33,1,22,45,6,9,10]))