tc = input("Lütfen Bir Tc kimlik numarası giriniz: ")
if tc[0] == "0":
    print("Tc kimlik Numarası 0 ile başlayamaz")
elif len(tc) != 11:
    print("Lütfen 11 rakam girdiğinize emin olun")
else:
    for i in range(len(tc)):
        if not tc[i].isdigit():
            print("Lütfen rakam olduğundan emin olun!!!")
            break
    else:
        tek_basamaklar = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
        cift_basamaklar = int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
        ilk_on_basamak = int(tc[0]) + int(tc[1]) + int(tc[2]) + int(tc[3]) + int(tc[4]) + int(tc[5]) + int(tc[6]) + int(tc[7]) + int(tc[8]) + int(tc[9])
        x = (tek_basamaklar * 7) - cift_basamaklar
        if ((x % 10) == int(tc[9])) and ((ilk_on_basamak % 10) == int(tc[10])):
            print("Tc kimlik Numaranız doğrudur!!!")
        else:
            print("Kimlik Numarası standartlarımıza uygun değildir!\nBöyle bir kayıt bulunamadı")
