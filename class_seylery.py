class Araba():  # sınıf tanımlanır (değişken grupları gibi)
    model = "R"
    renk = "kırmızı"
    beygir = "100"

araba1 = Araba()  # sınıfı değişkene tanımlar

print(araba1.beygir)

# ---------------------------------------------------

class some_stuf():

    def __init__(self, bir, iki, uc, dort = "sne"):  # değişken ve fonksiyon barındıran grup gibi?
        print("annex boi")
        self.bir = bir
        self.iki = iki
        self.uc = uc

stuf1 = some_stuf("iki", 7, "80")

print(stuf1.uc)

# ----------------------------------------------------

class Yazılımcı():
    
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maaş = maaş
        self.diller = diller
    def bilgilerigoster(self):  # İkinci bir metod tanımı
        print("""
        Çalışan Bilgisi:
        
        İsim :  {}
        
        Soyisim : {}
        
        Şirket Numarası: {}
        
        Maaş :  {}
        
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
 
yazılımcı1 =  Yazılımcı("X","Y",12345,3000,["Python","C","Java"])
 
yazılımcı1.bilgilerigoster()

# --------------------------------------------------------------------

class bruho():
    
    def __init__(self, a, b, c, d):
        print("bruho init fonksiyonları\n")
        
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def bilgilebnei(self):
        print("bruho değişkenleri:")
        print(self.a, self.b, self.c, self.d)
    
    def adegis(self, yenia):
        self.a = yenia
        
class kopyaci(bruho):   # parantez içine bir class yazarak onun metodları kalıtımla kopyalanır
    pass    # sonradan bir şeyler yazmak istiyorsak ya da boş bırakmak istiyorsak pass yazabiliriz, yoksa error verir

kopyaciDegiskeni = kopyaci("a", "2", 3, True)

kopyaciDegiskeni.bilgilebnei()

kopyaciDegiskeni.adegis("bruh")

kopyaciDegiskeni.bilgilebnei()

class kopyaci(bruho):  # pass yaptığı class'a devam ediyor
    
    def bir(self, cnew):
        self.c = cnew
    
kopyaciDegiskeni = kopyaci("a", "2", 3, True)

kopyaciDegiskeni.bir("pew")

kopyaciDegiskeni.bilgilebnei()

# ---------------------------------------------------------------------------

class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman
 
class Yönetici(Çalışan):
    
    def __init__(self,isim,maaş,departman,kişi_sayısı): # Sorumlu olduğu kişi sayısı
        super().__init__(isim,maaş,departman) # 3 tane özelliği Çalışan fonksiyonunun init fonksiyonuyla hallediyoruz.
        
        print("Yönetici sınıfının init fonksiyonu")
        
        self.kişi_sayısı = kişi_sayısı # Ekstra özelliği de kendimiz yazıyoruz.

# ---------------------------------------------------------------------

class Kitap():
    pass
 
kitap1 = Kitap() # __init__ metodu çağrılıyor.
print(kitap1) # __str__ metodu çağrılır.
del kitap1

class Kitap():
    
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    
    def __len__(self):
        return sayfa_sayısı
    
    def __del__(self):  # __del__ metodunu tanımladığımızda yine objeyi siliyor fakat ekstradan özellik eklemiş oluyosun
        print("kitap objesi go brr")
 
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye") # Kendi metodumuz

print(kitap1)

print(len(kitap1))

del Kitap

# -------------------------------------------------------------------------------