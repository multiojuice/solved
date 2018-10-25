dynamicMap = {}

def rob(nums):

    for index in range(0, len(nums)):
        dynamicMap[str(index)] = 0

    dynamicMap[str(len(nums) - 1)] = nums[-1]
    dynamicMap[str(len(nums) - 2)] = nums[-2]


    for index in range(len(nums) - 1, -1, -1):
        print(index)
        if not index - 2 < 0:
            print('\t', index-2)
            if dynamicMap[str(index)] + nums[index - 2] > dynamicMap[str(index - 2)]:
                dynamicMap[str(index - 2)] = dynamicMap[str(index)] + nums[index - 2]

        if not index - 3 < 0:
            print('\t', index-3)
            if dynamicMap[str(index)] + nums[index - 3] > dynamicMap[str(index - 3)]:
                dynamicMap[str(index - 3)] = dynamicMap[str(index)] + nums[index - 3]


    print(dynamicMap)
    return max(dynamicMap['0'], dynamicMap['1'])


print(rob([2,7,9,3,1]))

