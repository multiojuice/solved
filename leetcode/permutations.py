def permute(nums):
  """
  :type nums: List[int]
  :rtype: List[List[int]]
  """
  if len(nums) == 1:
    return [nums[0]]
  else:
    combos = []
    for num in nums:
      altNums = list(nums)
      altNums.remove(num)
      combos2 = permute(altNums)
      print('Comb 2',combos2)
      for combo in combos2:
        if (type(combo) == 'list'):
          combos.append([num] + combo)
        else:
          combos.append([num, combo])
    return combos
print(permute([1,2,3]))
