# ABSTRACTION
# ENCAPSULATION
# POLYMORPHISM
# INHERITANCE

student1 = {
    "name":"Jatin katiyar",
    "marks":50
}
student2 = {
    "name":"Smarath",
    "marks":100
}
print()

# Python object can have multiple attributes
#   - calllable (eg. functions and classes)
#   - iterable  (eg. list, string, generator)
#   - contextable   (eg. files)


class person:
    pass
p = person()
print(p)

print(hex(id(p)))

a = 1

class Person:
    def say_hi(self):
        print("Hello Everyone : ")

p = Person()
p.say_hi()

class Person:
    name = "Jatin"
    def say_hi(self):
        print(f"Hello Everyone : I am {self.name}")

p = Person()
p.say_hi()
Person.say_hi(p)