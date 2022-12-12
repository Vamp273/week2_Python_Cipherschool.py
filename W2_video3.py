def func():
    return 1 + 4
a1 = func
a1()

lambda a,b:a+b

show = print
show("something")

names = ("jatin", "sarah", "ahubham","samarath")
for name in names:
    print(name)

names1 = ("jatin", "sarah", "ahubham","samarath")
for name1 in enumerate(names1):
    print(name1)

a = 5
b = 9
temp = a
a = b
b = temp

a = 5
b = 9
a = a+b
b = a-b
c = a-b
print(a,b)

a = 5
b = 9
a,b = b,a
print(a,b)


#PACKING AND UNPACKING

names1 = ("jatin", "sarah", "ahubham","samarath")
for i,name in enumerate(names):
    print(i,"_", name)

names1 = ("jatin", "sarah", "ahubham","samarath")
scores = [50,70,90,80]

for i,name in enumerate(names):
    score = scores[i]
    print(name,"_",score)

names1 = ("jatin", "sarah", "ahubham","samarath")
scores = [50,70,90,80]

for a in zip(names,scores):
    print(a)

names1 = ("jatin", "sarah", "ahubham","samarath")
scores = [50,70,90,80]

for name,score in zip(names,scores):
    print(name,"_",score)

names1 = ("jatin", "sarah", "ahubham","samarath")
scores = [50,70,90,80]
states = ["delhi","punjab","up","haryana"]

for name,score,state in zip(names,scores,states):
    print(name,"_",score,state)