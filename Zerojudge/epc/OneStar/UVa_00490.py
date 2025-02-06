dic = {}
count = 0
L = 0
while True:
    try:
        In = input()
        dic[count] = In
        count += 1

    except EOFError:
        break

for i in range(count):
    L = max(L, len(dic[i]))

# print(L)

for i in range(L):
    str = ""
    for j in range(count):
        List = list(dic[j])
        try:
            if (List[i] == IndexError):
                pass
        except IndexError:
            if j == (count - 1) & i == L - 1:
                pass
            else:
                str = str + " "
                
        else:
            str = str + List[i]

    print(str[::-1])