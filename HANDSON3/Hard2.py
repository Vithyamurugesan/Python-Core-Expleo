def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def callback(operation, x, y):
    return operation(x, y)


print("Add:", callback(add, 5, 8))
print("Subtract:", callback(subtract, 20, 15))
print("Multiply:", callback(multiply, 7, 9))