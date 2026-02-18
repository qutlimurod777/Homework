# ismlar = []
#
# print("Yaqin do'stlaringizni ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (yes/no)")
#     if javob =='yes':
#         n+=1
#         continue
#     else:
#         break
# #1111111111111111111111111111111111111111111111111111111111111111111
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
#1111111111111111111111111111111111111111111111111111111111111111111
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()} ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#     javob = input("Yana ma'lumot qo'shasizmi? (yes/no)")
#     if javob == "no":
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
#111111111111111111111111111111111111111111111111111111111111111111111
# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars:  # nexia' in cars: bu Amal cars ichida nexia bormi yoqmi shuni tekshiradi
#     cars.remove('nexia')
# print(cars)
#11111111111111111111111111111111111111111111111111111111111111111111
talabalar = ['jonibek','husan','olim','botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()} ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi ")
    baholangan_talabalar[talaba] = baho



