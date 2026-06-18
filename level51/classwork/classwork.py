
# WHILE loop გამოიყენება მაშინ, როცა წინასწარ არ ვიცით რამდენჯერ განმეორდება —
# ციკლი მუშაობს მანამ, სანამ  არის TRUE .
# FOR loop გამოიყენება მაშინ, როცა წინასწარ ვიცით რამდენჯერ უნდა განმეორდეს მოქმედება.


correctPassword = "12345"

# მომხმარებლის მიერ შეყვანილი პაროლი თავდაპირველად ცარიელია
password = ""

# while ციკლი იმუშავებს მანამ, სანამ შეყვანილი პაროლი არ არის სწორი
while password != correctPassword:
    password = input("password: ")
    if password != correctPassword:
        print("password error")

print("is successful")

#Indexing გამოიყენება ერთეული ელემენტის ასაღებად.ინდექსი სიაში იწყება 0-დან.

#slisling მოიყენება მრავალი ელემენტის, ამოსაღებად.





