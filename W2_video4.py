a = 5
print("value of a is %d"%(a))
print("value of a is {}".format(a))

a,b,c = 1,2,3
d = "a={}, b={}, c ={}".format(a,b,c)
print(d)

name = "Jatin Katiyar"
company = "shuttl"

res = "name = {name} company = {company}".format(name=name,company=company)
res1 = f"Hello {name} welcome to my Facebook".format(name=name,company=company)
print(res)
print(res1)

print(f"name = {name}")

d = len(r"a\nb")
print(d)

for c in r"a\nb":
    print(c)

n = "     jatin   ".strip()
print(n)

m = "1,2,3,4,5,6".split(",")
print(m)

o = "jatin katyar".replace("a","z")
print(o)

p = "jatin katyar".count("a")
print(p)