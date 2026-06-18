
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("0 goa:", list[0])
print("1 goa:", list[1])
print("2 goa:", list[2])
print("3 goa:", list[3])
print("4 goa:", list[4])


list[0] = 9
list[2] = 8
list[4] = 7
list[6] = 6
list[8] = 5


print("goa:")
print(list)



 #ფუნქცია — ეს არის კოდის , რომელსაც შეგვიძლია სახელი დავარქვათ და საჭიროების დროს გამოვიძახოთ.
def goa (goa, name):
    print (goa + name)

 # def ნიშნავს define, ანუ ფუნქციის განსაზღვრა.
 #def-ის შემდეგ იწერება:ფუნქციის სახელი, ფრჩხილებში არგუმენტები , ბოლოს — ორწერტილი :

