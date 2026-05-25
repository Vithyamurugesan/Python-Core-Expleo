total = int(input("Enter total animals: "))
rabbit = int(input("Enter rabbit count: "))
deer = int(input("Enter deer count: "))
birds = int(input("Enter birds count: "))
squirrel = int(input("Enter squirrel count: "))
counted_total = rabbit + deer + birds + squirrel
if counted_total < total:
    print("Baby lion is mischievous")
elif counted_total == total:
    print("Baby lion is well behaved")
else:
    print("Counted wrongly")