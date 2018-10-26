dynamicMap = {}

def rob(nums):

    for index in range(0, len(nums)):
        dynamicMap[str(index)] = 0

    dynamicMap[str(len(nums) - 1)] = nums[-1]
    dynamicMap[str(len(nums) - 2)] = nums[-2]


    for index in range(len(nums) - 1, -1, -1):
        if not index - 2 < 0:
            if dynamicMap[str(index)] + nums[index - 2] > dynamicMap[str(index - 2)]:
                dynamicMap[str(index - 2)] = dynamicMap[str(index)] + nums[index - 2]

        if not index - 3 < 0:
            if dynamicMap[str(index)] + nums[index - 3] > dynamicMap[str(index - 3)]:
                dynamicMap[str(index - 3)] = dynamicMap[str(index)] + nums[index - 3]


    return max(dynamicMap['0'], dynamicMap['1'])


print(rob([500, 4 , 100 , 200 , 101]))
print(rob([500, 4 , 100 , 200 , 50]))
print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))

