a = 7
b = 5
print(a+b)
print("Waiting....")
print("Waiting....")
print("Waiting....")

print(a-b)
print("Waiting....")
print("Waiting....")
print("Waiting....")

print(a*b)
print("Waiting....")
print("Waiting....")
print("Waiting....")


x = 6
x1 = 'jatin'
x2 = 1.5
x3 = 'print'

def show_loading():
    for i in range(3):
        print("loading","."*(i+1))

print(a+b)
show_loading()

print(a-b)
show_loading()

print(a*b)
show_loading()

def sheldon_knock(name):
    for _ in range(3):
        print("knock knock knock", name)

sheldon_knock("leonard")

def sheldon_knock(name,times = 3):
    for _ in range(times):
        print("knock knock knock", name)

sheldon_knock("leonard")  

def add(n,m):
    return n+m

o = add(1,2)
print(o)