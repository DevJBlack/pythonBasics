Test your knowledge.
Answer the following questions

Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.

Double Click HERE to edit this markdown cell and write answers.

Numbers: Numbers in python is whole numbers, examples (100, 200,1,2,3,4)

Strings: Strings can be in double quote or single quote in python "Hello world" 'hello world'

Lists: Lists are muteable data and can be ordered example [1,2,3,4,5] they are also in sqaure brackets
t = [1,2,3,4,5]
t[0] = 4
t = [4,2,3,4,5]
This is ok in lists

Tuples: Tuples are similar like lists, but Tuples are in () and are immutable, they cant be changed.
tuple = (1,2,3,4,5)
tuple[1] = 5
would give an error

Dictionaries: Dict are key value pairs, they are unsorted, but you can call them by values or keys
dict = {"key1":"value", "key2":1.99,"key3": 1}

Numbers
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Solution: 2**2*4+300.50/2-66

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25


Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:


s = 'hello'
x
s[1]

Reverse the string 'hello' using slicing:
s[::-1]



Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
s[-1]
s[-1:]



d = {'simple_key':'hello'}
# Grab 'hello'

d['simple_key']

'hello'

d = {'k1':{'k2':'hello'}}
# Grab 'hello'

d['k1']['k2']

'hello'

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# This was harder than I expected...
d['k1'][0]['nest_key'][1][0]

'hello'

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

# Phew!
d['k1'][2]['k2'][1]['tough'][2][0]



# if, elif and else, have whitespace and do not use curly brackets. They also do not use || or && but use the words "or" and "and"

hungry = False

if hungry:
    print("Feed me!")
else:
    print("I already ate")

  loc = "Shop"

if loc == "Auto Shop":
    print("Cars are the stuff")
elif loc == "bank" or loc == "Bank":
    print("Money is cool")
else:
    print("I do not know where I am at")  

name = "Frankie"
names = "Devin Black"

if name == "Frankiln":
    print("Hello %s" % name)
elif name == "Devin":
    print("Devin, Hello")
else:
    print(f"What is your name? : It is {name}")


# FizzBuzz solution, one of them
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for newList in list:
    if newList%3 == 0 and newList%5 == 0:
        print("FizzBuzz")
    elif newList%5 == 0:
        print("Buzz")
    elif newList%3 == 0:
        print("Fizz")
    else:
        print(newList)

# ============================================
# First number is where it starts, second number is where it is going to, the thrid number is how many steps it will take.
# This example with start at 50, go in steps of 10 and end at 100
# 50, 60, 70, 80, 90,100

for num in range(50, 101, 10):
    print(num)

for ky in range(100,1):
    print(ky)