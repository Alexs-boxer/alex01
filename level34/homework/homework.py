#ფუნქციები საჭიროა იმისთვის, რომ კოდი უფრო მარტივად წასაკითხი, გასაგები და  გამოყენებადი იყოს
def double_values(numbers):
    return [x * 2 for x in numbers]
print(double_values([1, 2, 3, 4]))  


def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]
print(even_numbers([1, 2, 3, 4, 5, 6]))  



def squared_values(numbers):
    return [x ** 2 for x in numbers]
print(squared_values([1, 2, 3, 4]))  



def only_vowels(text):
    vowels = "aeiou"
    return "".join([ch for ch in text if ch in vowels])
print(only_vowels("გამარჯობა")) 



def negative_numbers(numbers):
    return [x for x in numbers if x < 0]
print(negative_numbers([-5, 3, -2, 7, -8]))


def positive_numbers(numbers):
    return [x for x in numbers if x > 0]
print(positive_numbers([-5, 3, -2, 7, -8]))



def square_times_ten(num):
    return (num ** 2) * 10
print(square_times_ten(5)) 


def power(x, y):
    return x ** y
print(power(2, 3))