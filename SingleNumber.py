def Single_Number(array):
    test=0
    for j in array:
        test ^=j
    return test

array1= [2,2,1]
array2= [4,1,2,1,2]

print(Single_Number(array1))
print(Single_Number(array2))
