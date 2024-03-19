### EDA YALÇINDAĞ #####

import random
hak = 10
tuttugum_sayi = random.randint(1, 100)
for i in range(hak):
    tahmin_sayi = int(input("Lütfen Tahmin sayınızı yazın : "))
    if(tuttugum_sayi==tahmin_sayi):
        print("Tebrikler Tuttuğum sayıyı doğru bildiniz!!")
        break
    elif(tahmin_sayi>tuttugum_sayi):
        hak = hak-1
        print(f"AŞAĞI\nKalan Hak sayınız: {hak}")
    else:
        hak=hak-1
        print(f"YUKARI\nKalan Hak sayınız:{hak}")
if(hak==0):
    print(f"Haklarınız Tükendi. Tuttuğum sayı {tuttugum_sayi} idi.")
