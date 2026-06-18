def manual_find(text, char):
    for i in range(len(text)):
        if text[i] == char:
            return i   # ვაბრუნებთ პირველი შეხვედრის ინდექსს
    return -1   # თუ ვერ ვიპოვეთ



# print(manual_find("python", "t"))   # 2
# print(manual_find("hello", "z"))    # -1

# def manual_count(numbers, target):
#     count = 0
#     for num in numbers:
#         if num == target:
#             count += 1
#     return count
# print(manual_count([1, 2, 3, 2, 4, 2, 5], 2))  # 3
# word = "python"

# print("y" in word)       # True  ("y" არის "python"-ში)
# print("z" not in word)   # True  ("z" არ არის "python"-ში)

# numbers = [1, 2, 3, 4, 5]
# print(3 in numbers)      # True
# print(10 not in numbers) # True
# manual_replace (space → '-')

# def manual_replace(text):
#     result = ""
#     for char in text:
#         if char == " ":
#             result += "-"
#         else:
#             result += char
#     return result
# print(manual_replace("hello world python"))  
# # "hello-world-python"