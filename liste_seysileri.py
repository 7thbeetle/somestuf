denme = ["a", 1, "d", "5", 0]
print(denme, "\n")
denme.insert(2, "pki")  # "listeadi.instert(gelmesini_istediğimiz_sıra, değer)" listeye seçili sıraya değer ekler
print(denme, "\n")

denme.append("taam")  # liste sonuna değer ekler "listeadi.append(değer)"
print(denme, "\n")

denme.pop()  # listnin seçili elemanını çıkarır, değer girilmediyse sondakini çıkarır "listeadi.pop(sıra)"
print(denme)
denme.pop(2)
print(denme, "\n")

liste1 = [1, 2, 3, 4, 5]
liste2 = [i * 2 for i in liste1]  # listenin elemanlarının değerlerini ikiyle çarpar
print(liste2, "\n")

bruh = ["tuna", "pro", "1234"]
bruhs = "/".join(bruh)  # listenin elemanlarının arasına yazılanı koyup string olarak birleştirir
print(bruhs)  # tuna/pro/1234

bruh.reverse()  # listenin elemanlarının sırasını ters çevirir
bruh.sort()  # baş harflere göre sıralar

# liste fonksiyonlarının return değeri vardır!!!

# ---------------------------------------------------------------------