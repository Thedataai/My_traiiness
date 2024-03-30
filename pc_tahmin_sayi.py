alt_sinir = 1
ust_sinir = 100

while True:
    #47
    tahmin=((ust_sinir-alt_sinir)//2) + alt_sinir
    
    print("Tahminim: ",tahmin)
    
    cevap = input("(y)ukarı, (a)şağı, (b)ildin")
    
    if cevap == "y":
        alt_sinir = tahmin
        
    elif cevap == "a":
        ust_sinir = tahmin
    
    elif cevap == "b":
        print("Yaşasın,Bildim...")
        break
    if alt_sinir == ust_sinir:
        print("Hile yapıyorsun... Ben Oynamıyorum")
