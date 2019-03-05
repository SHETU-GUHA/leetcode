class Solution(object):

  def twoSum(self, nums, target):

    if len(nums) <= 1:
      return False
    seen = {}
    for j in range(len(nums)):
      if nums[j] in seen:
        return [seen[nums[j]], j]
      else:
        seen[target - nums[j]] = j

  print twoSum(object, [2, 7, 11, 15], 9)
 

