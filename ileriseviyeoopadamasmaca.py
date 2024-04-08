import random

class AdamAsmaca:
    def __init__(self):
        self.kategoriler = {"hayvanlar": "C:/Users/erayc/OneDrive/Masaüstü/hayvanlar.txt", "isimler": "C:/Users/erayc/OneDrive/Masaüstü/isimler.txt", "sehirler": "C:/Users/erayc/OneDrive/Masaüstü/sehirler.txt"}
        self.puan = 0
        self.kelime = ""
        self.tahminler = []
        self.gizli_kelime = []
        self.adam_asmaca_gorselleri = [
            """
              --------
              |    |
              |
              |
              |
              |
            """,
            """
              --------
              |    |
              |    O
              |
              |
              |
            """,
            """
              --------
              |    |
              |    O
              |    |
              |
              |
            """,
            """
              --------
              |    |
              |    O
              |   /|
              |
              |
            """,
            """
              --------
              |    |
              |    O
              |   /|\
              |
              |
            """,
            """
              --------
              |    |
              |    O
              |   /|\
              |   /
              |
            """,
            """
              --------
              |    |
              |    O
              |   /|\
              |   / \
              |
            """
        ]

    def oyun_basla(self):
        kategori = self.kategori_sec()
        self.kelime = self.kelime_sec(kategori)
        self.gizli_kelime = ["-" for i in range(len(self.kelime))]
        self.oyun_dongusu()

    def kategori_sec(self):
        while True:
            print("Lütfen bir kategori seçin:")
            for i, kategori in enumerate(self.kategoriler.keys(), 1):
                print(f"{i} - {kategori}")
            secim = input()
            if secim.isdigit() and 1 <= int(secim) <= len(self.kategoriler):
                return list(self.kategoriler.keys())[int(secim) - 1]

    def kelime_sec(self, kategori):
        with open(self.kategoriler[kategori], "r") as f:
            try:
                kelimeler = f.readlines()
            except UnicodeDecodeError:
                f = open(self.kategoriler[kategori], "r", encoding="utf-8")
                kelimeler = f.readlines()
                
        return kelimeler[random.randint(0, len(kelimeler) - 1)].strip().lower()

    def oyun_dongusu(self):
        adim = 0
        while True:
            self.oyun_durumu(adim)
            tahmin = self.harf_tahmin()
            if tahmin in self.tahminler:
                print("Bu harfi daha önce tahmin ettiniz.")
                continue
            self.tahminler.append(tahmin)
            if tahmin in self.kelime:
                self.puan += 5
                for i, harf in enumerate(self.kelime):
                    if harf == tahmin:
                        self.gizli_kelime[i] = harf
            else:
                adim += 1
            if self.gizli_kelime == list(self.kelime):
                print("Tebrikler! Kelimeyi buldunuz: ----> ", self.kelime)
                print(f"Puanınız: {self.puan}")
                break
            if adim == len(self.adam_asmaca_gorselleri) - 1:
                print("Maalesef bilemediniz. Kelime:", self.kelime)
                break

    def oyun_durumu(self, adim):
        print("-" * 20)
        print(f"Puanınız: {self.puan}")
        print("Kelime:", "".join(self.gizli_kelime))
        print("Tahminleriniz:", ", ".join(self.tahminler))
        print(self.adam_asmaca_gorselleri[adim])
        print("-" * 20)

    def harf_tahmin(self):
        while True:
            tahmin = input("Bir harf tahmin edin: ").lower()
            if len(tahmin) == 1 and tahmin.isalpha():
                return tahmin


while True:
    oyun = AdamAsmaca()
    oyun.oyun_basla()
    a = input("Tekrar oynamak ister misin?")
    if a == "e":
        continue
    else:
        break
