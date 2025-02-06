while True:

    i, j = map(str, input().split())

    Max = max(len(i), len(j))
    ans = ""
    count = 0

    if i == j == "0":
        break

    Inv_i = i[::-1]
    Inv_j = j[::-1]
    for x in range(abs(len(i) - len(j))):
        if int(i) > int(j):
            Inv_j = Inv_j + "0"
        else:
            Inv_i = Inv_i + "0"

    # print(Inv_i, Inv_j)

    print(Inv_i[0])
    for x in range(Max):
        if (int(Inv_i[x]) + int(Inv_j[x])) > 9:
            count += 1
            if int(Inv_i[x+1]) < 9:
                Inv_i[x+1] = str(int(Inv_i[x+1]) + 1)
            elif int(Inv_i[x+1]) == 9:
                Inv_i[x+1] = "0"

def count_1(int n, str s0):
    s0[n+1] = 