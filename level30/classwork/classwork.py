
def  number(n):
    for i in range(1,n+1):
       print(i)

def greet(name):
    print("Hello " + name)
greet("Ixvis Tolma")

def multiply(a, b):
    result = a * b
    print(result)

def list(lst):
    list = []
    for i in range(len(lst)-1, -1, -1):
        list(lst[i])
    print(lst)

def number (numbers):
    result = []
    for num in numbers:
        if num > 10:
            result(num)
    return result

list = [3, 12, 7, 15, 10, 22, 1]
nam= number(list)
print(nam)

def sum(list, list2):
    sum1 = 0
    for num in list:
        sum1 += num

    sum2 = 0
    for num in list2:
        sum2 += num

    result = sum1 * sum2
    return result
