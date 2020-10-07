# arrr = [1,2,3,5]

# def findNumber(arr, k):
#     if k in arr:
#         print("YES")
#     else:
#         print("NO")
#     # for a in arr:
#     #     if a == k:
#     #         print("Yes")
#     #     elif a != k:
#     #         print(" ")
#     #     else:
#     #         print("No")
        
# findNumber(arrr, 4)

def oddNumbers(l, r):
    for i in range(l, r+1):
        if i%2 != 0:
            print(i)
    
oddNumbers(2,5)

def oddsNumbers(l, r):
    newArray = []
    for lo in range(l, r+1):
        if lo%2 != 0:
            newArray.append(lo)
    return newArray


