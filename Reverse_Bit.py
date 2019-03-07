def Reverse_Bits(n):
         test=0
         for j in range(32):
             test <<=1
             test |= n&1
             n>>= 1
         return test
print(Reverse_Bits(8320))
