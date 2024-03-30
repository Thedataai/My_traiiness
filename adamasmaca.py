### ADAM ASMACA OYUNU #####
import random

hayvanlar = ["inek","koyun","keçi","kedi","köpek","kertenkele"]

sayi = random.randint(0,len(hayvanlar)-1) ### listedeki indeksler 0 dan başladığı için len(0,1,2,3,4,5) = 6 ama listedeki 6.indeks olmadığından -1 yapıyor


kelime = hayvanlar[sayi]

cizgi = []

for i in kelime:
    cizgi.append("_")

hak = 5 + len(kelime)

while 1:
    print(cizgi)
    harf = input("Bir tahmin giriniz")
    
    
    if harf in kelime:
        for i in range(len(kelime)):
            if harf == kelime[i]:
                cizgi[i]=harf
    else:
        hak -= 1
        
    if "_" not in cizgi:
        print("Bildiniz Tebrikler...!!!!")
        break
    if hak <= 0:
        print("Hakkınız Tükendi!!!! Üzgünüm...")
