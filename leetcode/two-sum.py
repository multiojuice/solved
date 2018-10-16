"""
Owen Sullivan
for a list of numbers,
return the two instances that add together 
to be the given number, target
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numsLength = len(nums)
    for index1 in range(0, numsLength):
        if index1 != numsLength - 1:
            for index2 in range(index1 + 1, numsLength):
                if nums[index1] + nums[index2] == target:
                    return index1, index2
            
    return None

print(twoSum([0, 1, 5, 7, 60, 4, 52, 78, 90, 58], 57))
# (2,6) or 7 + 52 = 57