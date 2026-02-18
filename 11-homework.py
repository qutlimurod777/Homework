print(1)
fuqaro_0 ={'ism':'Mirzobek','yil':1985,'viloyat':'Samarqand'}
print(f"Otaming ismi {fuqaro_0['ism'].title()},\
 {fuqaro_0['yil']}-yilda,\
 {fuqaro_0['viloyat']} viloyatda tug'ilgan")

fuqaro_1 ={'ism':'Marifat','yil':1990,'viloyat':'Sirdaryo'}
print(f"Onaming ismi {fuqaro_1['ism'].title()},\
 {fuqaro_1['yil']}-yilda,\
 {fuqaro_1['viloyat']} viloyatda tug'ilgan")

fuqaro_2 ={'ism':'Muhammad','yil':2000,'viloyat':'Andijon'}
print(f"Akaming ismi {fuqaro_2['ism'].title()},\
 {fuqaro_2['yil']}-yilda,\
 {fuqaro_2['viloyat']} viloyatda tug'ilgan")

fuqaro_3 ={'ism':'Madamin','yil':2002,'viloyat':'Qarshi'}
print(f"Ukaming ismi {fuqaro_3['ism'].title()},\
 {fuqaro_3['yil']}-yilda,\
 {fuqaro_3['viloyat']} viloyatda tug'ilgan")

print(2)
oila_azoim_0 ={'ism':'Mansur','taom':'Osh'}
oila_azoim_1 ={'ism':'Robiya','taom':'Chuchvara'}
oila_azoim_2 ={'ism':'SHaxlo','taom':'Manti'}
oila_azoim_3 ={'ism':'Rustam','taom':'Shashlik'}
oila_azoim_4 ={'ism':'Rasulbek','taom':'xonim'}
oila_azoim_5 ={'ism':'Laylo','taom':'osh'}
print(f"{oila_azoim_0['ism'].title()},ning sevimli taomi{oila_azoim_0['taom']}")
print(f"{oila_azoim_1['ism'].title()},ning sevimli taomi{oila_azoim_1['taom']}")
print(f"{oila_azoim_2['ism'].title()},ning sevimli taomi{oila_azoim_2['taom']}")
print(f"{oila_azoim_3['ism'].title()},ning sevimli taomi{oila_azoim_3['taom']}")
print(f"{oila_azoim_4['ism'].title()},ning sevimli taomi{oila_azoim_4['taom']}")
print(f"{oila_azoim_5['ism'].title()},ning sevimli taomi{oila_azoim_5['taom']}")

print(3)
ATAMALAR = {'strip':'Barcha probellarni olib tashlaydi',
                 'float':'Real son',
                 'reverse':'Rõyhatni tersaki qiladi',
                 'title':'Har bir sõzni bosh harifini katta qiladi',
                 'capitalize':'Birinchi sõzni birinchi harifini katta qiladi',
                 'upper':'Hamma harfni katta qiladi',}
for ATAMA in ATAMALAR:
    print(f"{ATAMA.title()}: {ATAMALAR[ATAMA]}")
else:
 print("Bunday sõz atamasi mavjud emas")

print(4)

lugat = {
    "integer": "butun son",
    "float": "o‘nlik son",
    "string": "matn",
    "list": "ro‘yxat",
    "if": "agar",
    "else": "aks holda",
    "elif": "aks holda agar",
    "for": "uchun"
}
soz = input("So‘z kiriting: ").lower()

if soz in lugat:
    print("Tarjima:", lugat[soz])
else:
    print("Bunday so'z lug'atda mavjud emas")

print(5)
soz = input("Kalit so'zni kiriting: ")
s = soz.lower()

if s == "integer":
    print(f"{soz} so'zi Butun son deb tarjima qilinadi.")
elif s == "float":
    print(f"{soz} so'zi O'nlik son deb tarjima qilinadi.")
elif s == "string":
    print(f"{soz} so'zi Matn deb tarjima qilinadi.")
elif s == "list":
    print(f"{soz} so'zi Ro'yxat deb tarjima qilinadi.")
elif s == "if":
    print(f"{soz} so'zi Agar deb tarjima qilinadi.")
elif s == "else":
    print(f"{soz} so'zi Aks holda deb tarjima qilinadi.")
elif s == "elif":
    print(f"{soz} so'zi Aks holda agar deb tarjima qilinadi.")
elif s == "for":
    print(f"{soz} so'zi Uchun deb tarjima qilinadi.")
else:
    print("bunday so'z mavjud emas")







