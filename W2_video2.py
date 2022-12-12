print(1,2,3,4,5, sep = ",")

def func(a,b,c):
    print(a)
    print(b)
    print(c)

func(1,2,3)
func(c= 1,a=2,b=3)

def func():
    print("HELLO")

def funct(a):
    print(a)

func()
funct(1)

#ARGUMENTS IN PYTHON
#required argument
#default
#optional positional only argument
#required keyworded only argument
#default keyworded only argument
#optional keyworded only argument


def func(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)

func(1,2,3,4,5,6,7,d=8)

def func(a,b,*c,d,e="jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

func(1,2,3,4,d="something",e="andf")

def func(a,b=1,*c,d,e="",**k):
    print(k)

func(name="jatin")

# ANOMANOUS FUNCTION OR LAMBDA FUNCTION

lambda a,b: a+b