class Solution:
    def Isomorphic(self, s, t):
        return dict(zip(s, t)) == dict(reversed(list(zip(s, t)))) and dict(zip(t, s)) == dict(reversed(list(zip(t, s))))
s = Solution()
print (s.Isomorphic('paper', 'title'))
