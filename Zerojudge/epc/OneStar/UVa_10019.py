n = int(input())

for i in range(n):
    x = int(input())
    x1 = str(bin(x))
    x2 = ""
    for index, cher in enumerate(str(x)):
        if cher == "0":
            x2 = x2 + "0000"
        if cher == "1":
            x2 = x2 + "0001"
        if cher == "2":
            x2 = x2 + "0010"
        if cher == "3":
            x2 = x2 + "0011"
        if cher == "4":
            x2 = x2 + "0100"
        if cher == "5":
            x2 = x2 + "0101"
        if cher == "6":
            x2 = x2 + "0110"
        if cher == "7":
            x2 = x2 + "0111"
        if cher == "8":
            x2 = x2 + "1000"
        if cher == "9":
            x2 = x2 + "1001"
    c1, c2 = 0, 0

    for index, cher in enumerate(x1):
        if cher == "1":
            c1 += 1

    for index, cher in enumerate(x2):
        if cher == "1":
            c2 += 1

    print(c1, c2)