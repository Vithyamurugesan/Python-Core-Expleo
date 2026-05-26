#set ccnnot have the duplicates
my_set={1,2,3,4,3,2}
print(my_set)
print(my_set.pop())
#print(my_set.clear())
#print(my_set)


#we can make set from a list
my_set1=set([1,2,3,2,5,6])
print(my_set1)


#set cant have mutable items
#here [3,4] is a mutable list
#this will cause error
#my_set={1,2,[3,4]}


