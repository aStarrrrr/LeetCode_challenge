def check(nums):
    return sum(range(len(nums)+1)) - sum(nums)
arr = [3,0,1]
print(check(arr))