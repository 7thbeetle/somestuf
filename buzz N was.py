x = 0

l = []

while x < 101:
    s = x
    if (x % 15) == 0:
        s = "ikisinin de katı"
    elif (x % 3) == 0:
        s = "sadece 3'ün katı"
    elif (x % 5) == 0:
        s = "sadece 5'in katı"
    l.append(s)
    x += 1

for i in l:
    print(i, "\n")
