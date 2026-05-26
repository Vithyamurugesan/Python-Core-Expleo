#without using the list comprehension

ele=[]
for x in range(5):
    ele.append(x**2)
print(ele)


#Using the list comprehension

element=[x**2 for x in range(5)]
print(element)
