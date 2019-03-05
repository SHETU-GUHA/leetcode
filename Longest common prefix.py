class Solution:
   
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ''
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or str[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

s = Solution()
print s.longestCommonPrefix(["flower","flow","flight"])
print s.longestCommonPrefix(["aaa","aa","aa"])
