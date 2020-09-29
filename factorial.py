def factorial():
    f = 1
    a = int(input("sayı girke >>>   "))
    for i in range(1, a + 1):
        f *= i
    return f

while True:
    fac = factorial()
    print (fac)
