import random
import time
print("\n" * 500)

class kumanda():
    
    def __init__(self, tv_durum = False, tv_ses = 0, kanal_listesi = ["CN", "Disney Channel", "Nickelodeon"], kanal = "CN"):
        
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    
    def tv_ac(self):
        
        if (self.tv_durum == True):
            print("Televizyon zaten açıq")
        
        else:
            print("TV açılıyor...")
            time.sleep(1)
            print("%50")
            time.sleep(1)
            print("%100\nTV açıldy")
            self.tv_durum = True
    
    def tv_kapa(self):
            
        if (self.tv_durum == False):
            print("Televizyon zaten kapaly")
        
        else:
            print("TV kapandy")
            self.tv_durum = False
        
    def ses_ayarla(self):
            
        while True:
                
            print("""Sesi azalt: '<'\nSesi arttır: '>'\nÇıkmak için: 'bruh'""")
            c = input("\n>>>   ")
            
            if (c == ">" and self.tv_ses < 100):
                self.tv_ses += 10
                print("\ntv sesi:", self.tv_ses)
            
            elif (c == "<" and self.tv_ses > 0):
                self.tv_ses -= 10
                print("\ntv sesi:", self.tv_ses)
            
            elif (c == "bruh"):
                print("\nses son hal:", self.tv_ses)
                break
        
    def kanal_ekle(self):
        
        print("Kanal ismi gir ozmn")
        kanal_ismi = input("\n>>>   ")
        print("kanal eklenio")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendy")
    
    def kanalla_beni(self):
        
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("kanallar:", self.kanal_listesi,"\nŞu anki kanal:", self.kanal)
        
    def __len__(self):
            
        return len(self.kanal_listesi)
        
    def __str__(self):
            
        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\nŞu anki kanal: {}".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)

remote = kumanda()
yazi = """
      
      TV Remote stuf
      
      
      1) Tv aç
      
      2) Tv kapa
      
      3) Ses ayarla
      
      4) Kanal eqle
      
      5) Kanal sayısı öğren
      
      6) Rastgele kanala gech
      
      7) Tv bilgisy
      
      8) bu yazıyı gör
      
      çıkmak için 'bye' yaz köle
      
      not: bunu bne yazdım
      """

print(yazi)

while True:
    
    istek = input("\n>>>   ")
    print("\n")
    
    if istek == "1":
        remote.tv_ac()
    
    elif istek == "2":
        remote.tv_kapa()
    
    elif istek == "3":
        remote.ses_ayarla()
    
    elif istek == "4":
        remote.kanal_ekle()
    
    elif istek == "5":
        print("kanal sayısı:", len(remote))
    
    elif istek == "6":
        remote.kanalla_beni()
    
    elif istek == "7":
        print(remote)
    
    elif istek == "8":
        print(yazi)
    
    elif istek == "bye":
        print("you go brr")
        time.sleep(3)
        break
    
    else:
        print("düzgün yaz köle")


__credits__ = """yazan ben
derleyen ben
düşünen ben
thnx by"""
