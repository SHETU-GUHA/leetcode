class solution:
   def is_valid_parenthese(self, str):
        stack, char = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str:
            if parenthese in char:
                stack.append(parenthese)
            elif len(stack) == 0 or char[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(solution().is_valid_parenthese("()"))
print(solution().is_valid_parenthese("(){}[]"))
print(solution().is_valid_parenthese("()[{)}"))
print(solution().is_valid_parenthese("{[]}"))
print(solution().is_valid_parenthese("([)]"))

