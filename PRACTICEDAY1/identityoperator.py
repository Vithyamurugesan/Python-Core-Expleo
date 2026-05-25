#identity operator
num1=5
print(type(num1) is int)
num2=num1
print(id(num1))
print(id(num2))
print(num1 is not num2)

#membership operator
a=[1,2,3]
print(2 in a)
print('1' in a)
print(4 not in a)
print(3 not in a)


