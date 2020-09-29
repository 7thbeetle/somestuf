def stuf():  # herhangi bir parametre yok
    print("idk write sth here")


# --------------------------------------------------------------------------

def deneme(a, b):  # parametre tanımlaması, return ile değer dışarı çıkarılmış
    c = int(a) + int(b)
    return c * a + b


print("hal =", deneme(32, 17))


# output: hal = 1585


# --------------------------------------------------------------------------

def topla(a, b, c):  # sadece parametre tanımlaması
    print(a + b + c)


topla(1, 2, 30000)


# output: 30003


# --------------------------------------------------------------------------

def selamla(isim="boş adam"):  # parametre = varsayılan değer (opsiyoneldir)
    print(isim)


selamla()  # varsayılan değeri kullanılmış


# output: boş adam


# -------------------------------------------------------------------------

def sayilar(x=6, y=9, z=11):
    g = x + y * z
    return g


# output: 96


print(sayilar(z=10))  # sadece z parametresi için bir değer verilmiş, x ve y'nin varsayılan değeri kullanılmış

# -------------------------------------------------------------------------

print("write", "sth", "here", sep="/")  # sep parametresi ile araad boşluk yerine ne kullanılcağı yazılır


# output: write/sth/here

# -------------------------------------------------------------------------

def coklu(*u):  # başına yıldız koymak çoklu değişken yapar
    print(u)


coklu(1, 5, 7, 8, 4)


# output: (1, 5, 7, 8, 4)

# -------------------------------------------------------------------------

def coklu(*u, k):  # aynanda yanlızca 1 tane çoklu değişken kullanılabilir
    toplam = 0
    for i in u:
        toplam += i
    toplam *= k
    print(toplam)


coklu(5, 8, 10, 9, 5, k=7)  # yanına başka değişken konulursa tekli değişken belirtilmelidir
# output: 259

# -------------------------------------------------------------------------

L = 10


def ouch():
    print(L)  # L fonksiyon dışında tanımlandığından globaldir, istenilen yerde kullanılabilir, ama içince tanımlansaydı
    # local olurdu, dışarda ya da herhangi bir yerde kullanılamazdı


ouch()

# output: 10

# ------------------------------------------------------------------------

f = 7


def sth():  # değişken global olarak düzenlendiği için önceden verilen değerin üstüne yazar
    global f

    f = 5


sth()
print(f)
# output: 5

# -------------------------------------------------------------------------

def ikiylecarp(x):
    return x * 2
print(ikiylecarp(5))
# output: 10


# fonksiyonadı = lambda parametre1, parametre2... : işlem


ikiylecarpke = lambda x, y : x * y  # fonksiyonu tek seferde yazdı
print(ikiylecarpke(32, 2))
# output: 64

terslebeni = lambda x : x[::-1]
print(terslebeni("34k3 3kn3 mm43njn3k433b m3 j"))
# output: j 3m b334k3njn34mm 3nk3 3k43

# --------------------------------------------------------------------------

  