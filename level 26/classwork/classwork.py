def is_positive(number):
    if number > 0:
        return True
    else:
        return False
    
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
    

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print(is_positive(5))       
print(max_of_two(3, 10))
print(max_of_three(1, 7, 5))

def is_hot(temperature):
    if temperature >= 30:
        return True
    else:
        return False