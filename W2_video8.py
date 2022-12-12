a = []
for i in range(5):
    a.append(i)

print(a)

[i for i in range(5)]

a = []
for i in range(5):
    a.append(i**2)

print(a)

a = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j)
    a.append(temp)

print(a)


print([[ j for j in range(5) ] for i in range(5)])

n = 5
print([[ max(i+1,j+1,n-i,n-j) for j in range(n) ] for i in range(n)])

a = []
for i in range(2):
    for i in range(2):
        a.append(j)
print(a)

print([j for i in range(2) for j in range(2)])

print([[(i,j) for j in range(2)] for i in range(2)])

dict = {
    2:4,
    3:9,
    4:16,
}

print({i : i**2 for i in range(5)})

n = {i for i in range(5)}
print(type(a))

