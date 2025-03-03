def missing_element(n, arr):
    normal_sum = n*(n+1)//2
    current_sum = 0
    for data in arr:
        current_sum += data
    return normal_sum - current_sum
print(missing_element(6,[1,2,4,6,3]))