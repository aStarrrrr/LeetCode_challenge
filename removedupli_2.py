def remove_duplicates(arr):
    output_array = []
    for data in arr:
        if data not in output_array:
            output_array.append(data)
    return output_array
print(*remove_duplicates([1,2,2,3,3,4,5,5,6]))

#O(N^2)