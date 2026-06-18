n = int(input("შეიყვანე რიცხვი: "))
for i in range(0, n + 2):
    print(i)

i = int(input("შეიყვანე რიცხვი: "))
if i  == 0:
    print("ლუწი")
else:
    print("კენტი")

for i in range(1, 101):
    if i  == 0:
        print(f"{i} - ლუწი")
    else:
     a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))

if a > b:
    print(f"უფრო მაღალია: {a}")
elif b > a:
    print(f"უფრო მაღალია: {b}")
else:
    print("ორივე რიცხვი ტოლია")  
    print(f"{i} - კენტი")


name = input("შეიყვანე შენი სახელი: ")
for i in range(10):
    print(name)