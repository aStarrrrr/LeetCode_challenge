def check(nums):
    nums.sort()
    for i,data in enumerate(nums):
        if i != data:
            return data - 1
        if data == len(nums) - 1:
            return data + 1
arr = [2,0,1]
print(check(arr))