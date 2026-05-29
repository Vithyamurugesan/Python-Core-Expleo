class student:
    def __init__(self):
        self.name = "vithya"   # public
        self._age = 39         # protected

obj = student()

print(obj.name)    # calling public variable
print(obj._age)    # calling protected variable