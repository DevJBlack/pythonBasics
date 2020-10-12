def sayHello():
    print("Hello World")
    print("Hello USA")
    print("Hello Cyber")
sayHello()

def sayDefault(name="Default"):
    print(f"Hello {name}")
sayDefault()

def sayNew(name="Default"):
    print(f"Hello {name}")
sayNew("Devin")

def addNum(num1, num2):
    return num1 + num2
result = addNum(10,20)

def printResult(a,b):
    print(a+b)
printResult(10,20)

def returnResult(a,b):
    return a+b
addedResult = returnResult(10,20)
print(addedResult)

def myfunc(a,b):
    print(a+b)
    return a + b
newresult = myfunc(1,2)

