# print(1)
#
# shaxslar = [
#     {
#         "ism": "Abu Abdulloh Muhammad ibn Ismoil",
#         "t_yil": 810,
#         "t_joy": "Buxoro",
#         "umr": 60
#     },
#     {
#         "ism": "Abdulla Qodiriy",
#         "t_yil": 1894,
#         "t_joy": "Toshkent",
#         "umr": 44
#     },
#     {
#         "ism": "Erkin Vohidov",
#         "t_yil": 1936,
#         "t_joy": "Farg'ona",
#         "umr": 80
#     },
#     {
#         "ism": "Alisher Navoiy",
#         "t_yil": 1441,
#         "t_joy": "Xirot",
#         "umr": 60
#     }
# ]
#
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     yil = shaxs['t_yil']
#     joy = shaxs['t_joy']
#     umr = shaxs['umr']
#
#     print(f"{ism} {yil}-yilda {joy}da tavallud topgan. {umr} yil umr ko'rgan.")
#
# print(2)
#
# adiblar = {
#     "Abu Abdulloh Muhammad ibn Ismoil": [
#         "Al-jome' as-sahih",
#         "Al-adab al-mufrad",
#         "At-tarix al-kabir",
#         "At-tarix as-sag'ir"
#     ],
#     "Abdulla Qodiriy": [
#         "O'tkan kunlar",
#         "Mehrobdan Chayon",
#         "Obid ketmon"
#     ],
#     "Erkin Vohidov": [
#         "Tong nafasi",
#         "Qo'shiqlarim sizga",
#         "O'zbegim",
#         "Qiziquvchan Matmusa"
#     ],
#     "Alisher Navoiy": [
#         "Xamsa",
#         "Lison ut-Tayr",
#         "Mahbub ul-Qulub"
#     ]
# }
#
# for muallif, asarlar in adiblar.items():
#     print(f"\n{muallif} ning mashxur asarlari:")
#     for asar in asarlar:
#         print(asar)
#
# print(3)
#
# dostlar_kinolari = {
#     "Ali": [
#         "Terminator",
#         "Rambo",
#         "Titanic"
#     ],
#     "Vali": [
#         "Tenet",
#         "Inception",
#         "Interstellar"
#     ],
#     "Hasan": [
#         "Abdullajon",
#         "Bomba",
#         "Shaytanat"
#     ],
#     "Husan": [
#         "Mahallada duv-duv gap",
#         "John Wick"
#     ]
# }
#
# for ism, kinolar in dostlar_kinolari.items():
#     print(f"\n{ism}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)
#
print(4)
Davlat = input(f"Davlat nomini kiriting: ")

Davlatlar = {
    "O\'zbekiston":{
        "Poytaxt": "toshkent",
        "Aholisi": 33000000,
        "Pul": "So'm",
    },
    "Rossiya":{
        "Poytaxt":"Moskva",
        "Aholisi":144000000,
        "Pul":"Rubl"
    },
    "Aqsh":{
        "Poytaxt":"Vashington",
        "Aholisi":327000000,
        "Pul":"Dollar"
    },
    "ispaniya":{
        "Poytaxti":"Madrid",
        "Aholisi":3300000,
        "Pul":"Yevro",
    }
}

if Davlat in Davlatlar:
    print(f"{Davlat.upper()}")
    for kalit, qiymat in Davlatlar[Davlat].items():
        print(f"{kalit} {qiymat}")


else:
    print("Bunday davlat ro'yxatda yo'q")


































































