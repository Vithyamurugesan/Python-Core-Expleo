#emty dict 
my_dict={} 

#dict with integer keys
my_dict1={1:'apple',2:'ball'}

my_dict2={1:'CSE','name':'ram','list1':[1,2,3],'tuple':(4,5,6)}
print(my_dict2['name'])
print(type(my_dict2['list1']))

#using the keyword arguments
numbers=dict(x=5,y=0)
print(numbers)

#using mapping
numbers1=dict({'x':4,'y':5})
print(numbers1)

#using itearble
numbers2=dict([('x',5),('y',-5)])
print(numbers2)

#Nested dict 
students = {
    101: {
        "name": "Vithya",
        "age": 21,
        "course": "Python"
    },
    102: {
        "name": "Rahul",
        "age": 22,
        "course": "Java"
    }
}
print(students)
print(students[101]['name'])


#numbers1=dict({'x':4,'y':5})
for x in numbers1:
    print(x,numbers1[x])

print(numbers1.keys())    #it will shows keys as list format 
print(numbers1.values())

print(numbers1.pop(x))

d={1:"one",2:"two"}
d={2:"three"}
d.update(d)
print(d)
