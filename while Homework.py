print(1);

kitob = input("Siz yaxshi ko'rgan kitoblar nomini kiriting:")
while True:
    if kitob == {"stop"}: break
    kitoblar = ("Adabiyot", "Ona-tili", ",Matematika");
    if kitob in kitoblar:
        print(f"siz yoqtirgan kitob nomi{kitob}")
    else:
        print("kechirasiz bunday kitob mavjud emas")


print(2)
Yosh = input("Yoshingizni kiriting (exit/quit - chiqish): ")
while True:
    if Yosh.lower() == "exit" or Yosh.lower() == "quit":
        print("Dastur to‘xtadi.");
        break
    yosh = int(Yosh)

    if yosh < 7:
        print("Chipta narxi: 2000 so'm\n")
    elif yosh < 18:
        print("Chipta narxi: 3000 so'm\n")
    elif yosh < 65:
        print("Chipta narxi: 10000 so'm\n")
    else:
        print("Chipta bepul\n"); break


