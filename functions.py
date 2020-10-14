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

# =============================
def evenCheck(number):
    result = number % 2 == 0
    return result
    # Or for cleaner code
    # return number % 2 == 0 // Same code
evenCheck(20)

def checkEvenList(numList):

    for number in numList:
        if number % 2 == 0:
            return True
        else:
            pass
    return False

checkEvenList([1,3,5])
checkEvenList([2,4])
checkEvenList([1,2,3,4,5,6])

def evenList(listNum):
    # Placeholder variables
    evenNumber = []

    for number in listNum:
        if number % 2 == 0:
            evenNumber.append(number)
        else:
            pass
    
    return evenNumber

evenList([1,2,3,4,5])


stockPrices = [("appl",200), ("goog",400),("msft",100)]

for ticker,price in stockPrices:
    print(ticker)

for ticker,price in stockPrices:
    print(price+(0.1*price))

workHours = [("Abby", 1000), ("Billy",400), ("Cassie", 800)]

def employeeCheck(workHours):
    currentMax = 0
    employeeOfMonth = ""

    for employee,hours in workHours:
        if hours > currentMax:
            currentMax = hours
            employeeOfMonth = employee
        else:
            pass
    
    return(employeeOfMonth, currentMax)

name,hours = employeeCheck(workHours)
print(name, hours)
