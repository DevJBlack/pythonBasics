# def les_of_even(a,b):
#     if a %2 ==0 and b%2 == 0 and a < b:
#         print(a)
#     elif a %2 ==0 and b%2 == 0 and b < a:
#         print(b)
#     elif a %2 != 0 and b%2 != 0 and b > a:
#         print(b)
#     elif a %2 != 0 and b%2 != 0 and a > b:
#         print(a)
#     else:
#         pass
# les_of_even(2,9)

def les_even(a,b):
    if a%2 == 0 and b%2 == 0:
        # Both number are even
        if a < b:
            result = a
        else:
            result = b
    else:
        # One or both numbers are odd!
        if a > b:
            result = a
        else:
            result = b
    return result
result = les_even(7,5)
print(result)

def even_les(a,b):
    # Refactoring even more
    if a%2 == 0 and b%2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    return result
result1 = even_les(7,5)
print(result1)

def even_less(a,b):
    # Refactoring even more
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
result11 = even_less(1,5)
print(result11)

def animal_crackers(text):
    wordlist = text.upper().split()
    print(wordlist)
    first = wordlist[0]
    second = wordlist[1]
    print(first[0])
    print(second[0])
    print(first[0] == second[0])
    # Another way of doing it
    print(wordlist[0][0] == wordlist[1][0])
    
animal_crackers("Level Limam")

print("############################")

def makes_twenty(n1,n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20

    # if n1 + n2 == 20:
    #     return True
    # elif n1 == 20:
    #     return True
    # elif n2 == 20:
    #     return True
    # else:
    #     return False
twenty = makes_twenty(10,20)
print(twenty)

print("############################")

def old_mac(name):
    first_part = name[:3]
    second_part = name[3:]
    return first_part.capitalize() + second_part.capitalize()
mac = old_mac("macdonald")
print(mac)

print("###########################")

def master_yoda(text):
    worldlist = text.split()
    reverse_word_list = worldlist[::-1]
    return " ".join(reverse_word_list)
yoda_text = master_yoda("I am home")
print(yoda_text)

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)
there = almost_there(150)
print(there)

print("###########################")

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
thirty = has_33([1,3,3])
print(thirty)

print("###########################")

def paper_doll(text):
    result = ""
    for char in text:
        result += char*3
    return result
paper = paper_doll("Hello")
print(paper)

print("###########################")

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else:
        return "BUST"
jack = blackjack(5,6,7)
print(jack)

print("###########################")
print("This is the even_odd function")
def even_odd( x ):
    if (x % 2 == 0):
        return True
    else:
        return False
eo = even_odd(10)
print(eo)

print("###########################")
# my_number = input(print("Input a number:"))
# if int(my_number)%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num!=6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
sum69 = summer_69([2,1,6,9,11])
print(sum69)
    
print("#################### Challange problems")

def spy_game(nums):

    code = [0,0,7, "x"]

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
# sg = spy_game([1,2,3,0,0,7,6]) # True
# sg = spy_game([1,0,2,4,0,5,7]) # True
sg = spy_game([1,7,2,0,4,5,8]) # False
print(sg)

print("####################")

def count_primes(num):
    # Check for zero or one
    if num < 2:
        return 0
    # 2 or greater
    # 
    # Store our prime numbers
    primes = [2]
    # Counter going up to the input num
    x = 3
    # X is going through every nmber up to the input num
    while x <= num:
        # Check if x is prime
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
cp = count_primes(100)
print(cp)