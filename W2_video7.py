a = {1,2,3,4,5}
print(type(a))

print(list(a))

a.add(7)
a.remove(3)
a.add(2)

for i in a:
    print(i)

b = {1,2,3,7,4}
c = {5,4,6,7,8}

b.union(c)
b.intersection(b)

#is operator
# concept of mutable and unmuttable
# memory management in python

a =[['']*3]*3
a[1][1] = 'x'
print(a)

print(id(a[0][1]))
print(id(a[1][1]))
print(id(a[2][1]))

class student:
    name = "Tony"
    marks = 60

a = 555
b = 555
print(a is b)

n = "jatin"
print(hash(n))