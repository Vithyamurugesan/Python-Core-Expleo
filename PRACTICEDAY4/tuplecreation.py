#empty tuple
my_tuple1=()           

#tuple without the parentheses
my_tuple1=10,20,'ram','c'
print(type(my_tuple1))

#tuple with mixed datatype 
my_tuple2=(300,20,'ram','c')
print(type(my_tuple1[2]))

t=(10,20,30,40,50)
t=(100,)+t[1:]         # , for representing as the tuple otherwise it will take it as int
print(t)


addr='monty@python.org'
uname,domain=addr.split('@')
print(type(addr))
print(uname)
print(domain)

quot,rem=divmod(7,3)
print(quot)
print(rem)