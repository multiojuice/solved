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

      if type(combos2[0]) == list:
        print('in list')
        for combo in combos2:
          combo.insert(0,num)
      else:
        combos2.insert(0,num)
      combos.append(combos2)
    return combos

print(permute([1,2,3]))
