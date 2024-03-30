soru1 = ["...., gelir zamanı atasözündeki boşluğa hangi kelime grubu gelmelidir?","a-saatini sakla","b-sakla samanı","c-sakla hayvanı","d-sakla çorbayı","b"]
soru2 = ["Hangisi TRT Ankara Radyosu çok sesli korosu kurucularından biridir?","a-Adnan Saygun","b-Ahter Destan","c-muammer sun","d-İnci özdil","c"]
soru3 = ["python programlama dilinde hangi anahtar kelime bir döngüyü sonlandırmak için kullanılır","a-break","b-exit","c-end","d-broke","a"]
soru4 = ["hangi gezegen güneş sistemindeki en büyük gezegen olarak bilinir?","a-mars","b-jüpiter","c-venüs","d-merkür","b"]
soru5 = ["Çin seddi Nerededir?","a-Çin","b-Rusya","c-amerika","d-hindistan","a"]
soru6 = ["Hangi bilim dalı insan zihin sağlığının kalitesini arttırmak ve incelemek için oluşmuştur?","a-fizik","b-kimya","c-psikoloji","d-matematik","c"]

#Eğer isterseniz burada soru sayısını arttırabilirsiniz#

sorular = [soru1,soru2,soru3,soru4,soru5,soru6]
odul = 100
kontrol = True
for i in range(len(sorular)):
    for j in range(5):
        print(sorular[i][j]) #sorunun kendisi
        
    cevap = input("Cevabınız: ")
    if cevap == sorular[i][5]:
        odul *= 2
        print("Tebrikler Ödülünü",odul)
    else:
        print("Kaybettiniz")
        kontrol = False
        break
