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