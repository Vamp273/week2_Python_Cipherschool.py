a = [1,2,3,4]
print(a)

b = ["jatin",1,2.5,print]
print(b)

c = [1,2,3,4,5]
c[0]=100
print(c)

x = "jatin"
y = "katayr"
print(x+y)

n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]
print(n1+n2)

m = [1]*4
print(m)

p = [1,2,3,4,5]
for x in p:
    print(x)

z = "z" in "jatin"
print(z)

a = [1,2,3,4,5]
print(a[-1])

a = [1,2,3,4]
a.pop()

print(a)

f = ["jatin", "samarth", "shubham","sarathak"]
f.remove("sarathak")

e = [5,7,78,3,5,8,9,46,88,5,67,3,2,4,89,0,7,65]
sorted(e)

e.reverse()
reversed(e)

for x in reversed(e):
    print(x)

a = [1,2,3,4]
print(list(map(lambda x:x**2,a)))

for i,x in enumerate(a):
    pass

def sqr(x):
    return x**2

for x in map(lambda x: x**2, a):
    print(x)

a = input().split()

