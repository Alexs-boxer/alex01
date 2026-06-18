
names = ["გიო", "ანა", "საბა"]
name = ", ".join(names)
print("sentence")


animals = ["ბიზონი", "სირაქლემა","ზებრა" ]
animals.append("კუ")
print(animals)

 #დაბეჭდე სიის პირველი და ბოლო წევრი.(გამოიყენე ნეგატიური ინდექსები
a=[1,2,3,4,5,6,]
list = ["გიო", "ანა", "საბა", "ნიკა"]

# პირველი ელემენტი ნეგატიური ინდექსით: -len(სია)
first = list[-len(list)]

# ბოლო ელემენტი ნეგატიური ინდექსით: -1
last = list[-1]

print(" პირველი")
print("ბოლო") 

#დაწერე სტრინგი "მეგობრები" და გინდა გაიგე რამდენი ასოსა ამ სიაში. დაბეჭდე რაოდენობა
frends="მეგობრები"
print(frends.len() )

#:დაგიწერია სია [მე,მიყვარს,გოა] და გაიგე გაიგო რამდენი ელემენტია ამ სიაში. დაბეჭდე რაოდენობა
სია = ["მე", "მიყვარს", "გოა"]

goa = len(სია)

print("რაოდენობა")
 #შექმენი სია შენი საყვარელი 3 სიმღერა და დაუმატე მეოთხე სიმღერა "pantera" მეორე ინდექსზე
song = ["Numb", "Bohemian Rhapsody", "Smells Like Teen Spirit"]

song.insert(2, "pantera")

print("song")

list = ["Numb", "Bohemian Rhapsody", "pantera", "Smells Like Teen Spirit"]
# სიის გადაქცევა სტრინგად (გაერთიანება ერთ წინადადებად):
string= ", ".join("song")
print("string")
#გადააკეთე სტრინგი ჯერ  დიდ ასოებად მერე პატარად და საბოლოოდ პირველ ასო გაზარდე
text = "string"
print(text.upper())
print(text.lower())
print(text.capitalize())

#იპოვე სიტყვა "პითონი" წინადადებაში find() ფუნქციით და დაბეჭდე მისი მდებარეობა.
sentence = "i love python"
position = sentence.find("puthon")
print("python")