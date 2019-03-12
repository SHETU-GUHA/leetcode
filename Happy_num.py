class Solution:
    def Happy_num(self, n):
        def process(x):
            sum = 0
            while x:
                sum += (x % 10) ** 2
                x /= 10
            return sum

        a = process(n)
        b = process(a)
        while a != 1 and a != b:
            a = process(a)
            b = process(b)
            b = process(b)

        return 1 == a

sum = Solution()
print sum.Happy_num(19)
