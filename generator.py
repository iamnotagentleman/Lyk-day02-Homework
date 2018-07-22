import random
class Generator():
    def namegenerator(self):
        rand_int = random.randint(0,12)
        name_dict = {
         0 : "Serhat",
         1 : "Fatih",
         2 : "Evren",
         3 : "Veli",
         4 : "Burcu",
         5 : "Buse",
         6 : "Ali",
         7 : "Ankaralı Namık",
         8 : "Hakan",
         9 : "Ahmet",
         10 : "Derya",
         11 : "Mehmet",
         12 : "Songül",}
        return name_dict.get(rand_int)
    def surnamegenerator(self):
        rand_int2 = random.randint(0,12)
        surname_dict = {
        0 : "Eroğlu",
        1 : "Karcı",
        2 : "Erikli",
        3 : "Bugs",
        4 : "Demir",
        5 : "Aktağ",
        6 : "Boztaş",
        7 : "Aslan",
        8 : "Züğürtoğulları",
        9 : "Özdoğan",
        10 : "işler",
        11 : "Jobs",
        12 : "Gates",
        }
        return surname_dict.get(rand_int2)
    def habergenerator(self):
        random_int3 = random.randint(0,6)
        olay_dict = {
        0 : "{} {}'in 3 Gün Yatmadan Yaptığı Proje'de Bug Bulan {} Developer Kayıp.",
        1 : "{} {}'ında içinde oldugu Python'mu Ruby mi Kavgasında {} kişi Gıdıklanrak Öldü. ",
        2 : "Şarkı dinlemesine izin verilmeyen {} {} Adlı Ergen Cinnet Geçirdi {} ölü",
        3 : "Kahve'yi Çok Seven Lyk Eğitmeni {} {}, Abanat Kahvecisi Kapanınca Cinnet Geçirdi {} Yaralı",
        4 : "Hava Alanı Olmayan Bolu'da {} {}'nın Kontrolunde Olan Boeing 747 Kazası {} Ölü. ",
        5 : "{} {} 'ında içinde bulunduğu Apple'mı Android'mi Kavgasında {} ölü Microsft Phone'cular Halinden Memnun.",
        6 : "{2} Yıllık Profosyonel Öğrenci Olan {0} {1} Universte Şeref Madalyası Aldı",
        }
        haber =  olay_dict.get(random_int3)
        haber = haber.format(self.namegenerator(),self.surnamegenerator(),random.randint(0,100))
        haber = haber.replace("('","")
        return haber
