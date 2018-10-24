def rob(nums):
    total1 = 0
    for index in range(0, len(nums), 2):
        total1 += nums[index]
    total2 = 0
    for index in range(1, len(nums), 2):
        total2 += nums[index]

    return max(total1,total2)

print(rob([]))

