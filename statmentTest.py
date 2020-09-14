# Use for, .split(), and if to create a Statement that will print out words that start with 's':


# st = 'Print only the words that start with s in this sentence'

# #Code here
st = 'Print only the words that start with s in this sentence'
x = st.split(" ")

for sletter in x:
    if sletter[0] == "s" or sletter[0] == "S":
        print(sletter)


# Use range() to print all the even numbers from 0 to 10.

# #Code Here
for num in range(0,10,2):
    print(num)
# Or this way
for num in range(0,10):
    if num%2 == 0:
        print(num)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

# Code Here
three = [element for element in range(1,50) if element%3 == 0]
three

# Go through the string below and if the length of a word is even print "even!"


# st = 'Print every word in this sentence that has an even number of letters'

st = 'Print every word in this sentence that has an even number of letters nothing odd will be printed'
even = st.split(" ")

for newEven in even:
    if len(newEven)%2 == 0:
        print(newEven)

# 
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".



for fb in range(1,101):
    if fb%5 == 0 and fb%3 == 0:
        print(f"{fb} FizzBuzz")
    elif fb%3 == 0:
        print(f"{fb} Fizz")
    elif fb%5 == 0:
        print(f"{fb} Buzz")
    else:
        print(fb)

# Use List Comprehension to create a list of the first letters of every word in the string below:

vt = 'Create a list of the first letters of every word in this string'
x = vt.split(" ")

for lc in x:
     print(lc[0])