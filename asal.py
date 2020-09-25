def asal():
    a = int(input("sayı girke >>>   "))
    i = (a // 2) + 1
    x = True

    while i > 1:
        if (a % i) == 0:
            i = 1
            x = False

        else:
            i -= 1

    if x == False or a == 1:
        print("Asal değildir")

    else:
        print("Asaldır")

while True:
    asal()
