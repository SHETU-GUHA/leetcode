def isPalindrome(s):

    rev = ''.join(reversed(s)) 
    if (s == rev): 
        return True
    return False

s = "121"
ans = isPalindrome(s) 
  
if (ans): 
    print("True") 
else: 
    print("False") 

