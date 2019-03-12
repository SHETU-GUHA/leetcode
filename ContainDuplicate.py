class Solution:
    def Duplicate(self, num):
        return len(set(num)) != len(num)

s = Solution()
print(s.Duplicate([1, 2, 3, 4]))
print(s.Duplicate([2, 2, 3, 4]))
