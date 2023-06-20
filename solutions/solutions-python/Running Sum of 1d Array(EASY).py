def runningSum(nums):
    li = []
    num = 0
    for i in nums:
        num += i
        li.append(num)
    return li

print(runningSum([1,2,3,4]))