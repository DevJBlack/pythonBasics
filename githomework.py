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