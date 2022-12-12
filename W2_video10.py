#   DUNDERS
#   (magic method)/(event method)

class A:
    def __init__(self):
        print(self)
        print("initiated")
    def __del__(self):
        print("Iam dying")

a = A()

class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person("Nikhil")
p.say_hi()

a = 1
print(a+1)

print(str(a))

for i in a:
    print(i)

class A1:
    a = 1
    b = 2

    def __add__(self,x):
        return self.a + self.b +x

a = A1()
print(a)