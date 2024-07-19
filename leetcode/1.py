nums = [3,3]
target = 6
def function(nums,target):
    for num in range(len(nums)):
        for i in range(len(nums)):
            if num == i:
                continue
            else:
                if nums[num]+nums[i] == target:
                    return [num,i]
print(function(nums,target))