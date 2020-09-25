def bolen():
    a = int(input("sayı girke >>>   "))
    l = range(1, (a // 2 + 1))
    bol = []
    
    for i in l:
        if a % i == 0:
            bol.append(i)
    bol.append(a)
    print(a, "'nın bölenleri: ", bol, sep="")

while True:
    bolen()
