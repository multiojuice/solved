"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4
"""
def lengthOfLIS(nums):
    valMap = {}
    for index in range(len(nums)):
        valMap[index] = [nums[index], 1]

    for index in range(len(nums)):
        for index2 in range(index, len(nums)):
