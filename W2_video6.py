a = [1,2,3,4]
a[0] = 100
a[2] = 200
print(a)

b = (1,2,3,4)
print(type(b))

def func(*args):
    print(type(args))

func(1,2,3,4)

a= 5
b =9
a,b = b,a

c = a,b
print(type(c))

def sum_diff(a,b):
    s = a+b
    d = a-b
    return s,d

print(sum_diff(10,5))

a = (1,2,3,4)
print(list(range(5)))
print(tuple(range(5)))

a = (1,2,3,4,5,6)
#a.append(8)  #tuple does not have append attribute

a = {
    "name":"Jatin katayar",
    "l":"something",
    (1,2):"tuple key wht?"
}
print(a["name"])
print(["l"])
print(a[(1,2)])


b = {
    "name":"jatin",
    "company":"shutti",
    "college":"LPU"
}

key = "marks"
if key in b:
    print(b[key])
else:
    print("key doesn't exist")

key = "marks"
print(b.get(key))

key = "name"
print(b.get(key,"key does't exist"))

print(b.values())

for x in b.items():
    print(x)

for key, value in b.items():
    print(key,"_>",value)

print(b)

for x in b:
    print(x)

my_dict = [
    {
        "roll-no":1211,
        "name":"Ravi",
        "branch":"CSE"
    },
    {
        "rool-no":202,
        "name":"Abhishek",
        "branch": "SE"
    },
    {
        "roll-no":1202,
        "name":"Sachin",
        "branch":"IT"
    }
]