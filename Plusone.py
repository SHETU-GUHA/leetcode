class Solution(object):
    def addOne(self, digits):

        if digits[-1] <5:
            digits[-1] = digits[-1] + 1
        else:
            if len(digits) == 1:
                digits = [1,0] 
            else:
                digits = self.addOne(digits[:-1])
        return digits
check= Solution()
num1 = [6,3,2,1]
num2= [4,3,2,1]
print check.addOne(num1)
print check.addOne(num2)
