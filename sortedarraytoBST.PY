class TreeNode:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

class Solution:
	
	def sortedarraytoBST(self, nums):
		if len(nums) == 0:
			return None
		centerIndex = len(nums)/2
		center = TreeNode(nums[centerIndex])
		center.left = self.sortedarraytoBST(nums[:centerIndex])
		center.right = self.sortedarraytoBST(nums[centerIndex+1:])
		return center


temp = Solution()
res = temp.sortedarraytoBST([-10,-3,4,0,5,9])
print res.data
print res.left.data
print res.left.right.data
print res.right.data
print res.left.left.data 
print res.right.left.data

