class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 500,
            100, 50,
            10, 5, 
            1
            ]
        syb = [
            "M","D", 
            "C","L",
            "X","V",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(10))
print(py_solution().int_to_Roman(55))
