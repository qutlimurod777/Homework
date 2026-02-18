# # Lug'at elementlari bilan ishlash

# men ={
#     'ism':'Qutlimurod',
#     'familiya':'Zaripov',
#     'yosh':22,
#     'Fakultet':'Telekamunikatsiya texnalogiya fakulteti',
#     'Kurs':4
# }
# # print(men.items())
# for kalit, qiymat in men.items():
#     print(f"kalit: {kalit}")
#     print(f"qiymat: {qiymat} \n")
###############################################################################################################
print("Do'kondagi mahsulotlar")
mahsulotlar ={ # Dokondagi mahsulotlar
 'olma':12000,
 'anor':21000,
 'shaftoli':25000,
 'xurmo':17000,
 'olcha':22000,
  'dragon':55000
 }
# print(mahsulotlar.keys())
for mahsulot in mahsulotlar.keys():
 print(mahsulot.title())

Bozorlik =['xurmo','banan','uzum','olma','olcha','shaftoli']
for mahsulot in mahsulotlar:
 if mahsulot in Bozorlik:    #mahsulot borlikini tekshirish
   print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

Bozorlik =['xurmo','banan','uzum','olma','olcha','shaftoli']
for Buyum in mahsulotlar:
 if Buyum not in Bozorlik:
  print(f"Iltimos do'koningizda {Buyum} ham olib keling")

print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):   #Mahsulotlarni Alifbo bo'yicha taxlaydi
    print(mahsulot.title())            #sorted(mahsulotlar, reverse=True): Bu Alifboni teskari tartibda taxlaydi

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'
    }

# print(telefonlar.values())

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)






































