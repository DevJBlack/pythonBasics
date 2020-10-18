def myfunc(a,b):
    # Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05
result = myfunc(40,60)
print(result)

def mynewfunc(*args):
    return sum(args) * 0.05
newResult = mynewfunc(1,2,100,120)
print(newResult)

def myForFunc(*args):
    for item in args:
        print(item)
myForFunc(1,5,10,15,20)

def myfunckwag(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is %s" % kwargs["fruit"])
    else:
        print("I did not find any fruit here")
myfunckwag(fruit = "Peach", veggie = "Spinach")

def myfunnyfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print ("I would like %s" % args[0], kwargs["food"])
myfunnyfunc(10,20,30, fruit = "oranage", food = "eggs", animale = "dog")

# *args is a tuple that we can pass as many values as we want
# **kwargs is a dict that we can pass as many key word values into it.

def myfuncc(*args):
    luck = []
    for item in args:
        if item %2 == 0:
            luck.append(item)
        else:
            pass
    return(luck)
dev = myfuncc(5,6,7,8)
print(dev)

def skyline(str):
    test = ""
    letterTest = 1
    for sky in str:
        if letterTest % 2 ==0:
            test += sky.upper()
        else: 
            test += sky.lower()
        letterTest += 1 
    return test
line = skyline("Anthropomorphism")
print(line)