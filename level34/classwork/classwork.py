#ფუნქცია გამოიყენება სტრიქონის გასაყოფად.
frut = "apple,whatermallon,banana "
eat = frut.split()
print(eat)
#გამოიყენება სტრინგების სიაში ელემენტების ერთმანეთთან შეერთებისთვის ერთ მთლიან სტრინგად.
country= ["rusia", "uzbekistan", "georgia"]
europ = " ".join(country)


def sum_two_number(a, b):
    return a + b

print(sum_two_number(3, 5))