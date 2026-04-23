def fun1():
    print("hello function")
# fun1()

def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1) 
# print(fact(3))

def findMax(a,b,c):
    return max(a,b,c)
# print(findMax(15,65,81))


def sumNatural(n):
    if(n==1):
        return 1
    return n+sumNatural(n-1)
# print(sumNatural(15))

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
# pattern(30)

def remove(ls, word):
    newls = []
    for items in ls:
        if not(items == word):
            newls.append(items.strip(word))
    return newls

ls  = ["pranav", "anand", "aman", "riya", "mummy", "an"]
print(remove(ls,"an"))