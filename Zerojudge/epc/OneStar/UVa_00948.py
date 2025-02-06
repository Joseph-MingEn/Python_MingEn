n = int(input())
num = []
Max = 0
Fibs = []
count = 0
for i in range(n):
    j = int(input())
    num.append(j)
    Max = max(Max, j)

# print(Max)
tump = 1
o = 1
while True:
    # print("o =",o, "tump =", tump)
    Fibs.append(o)
    tumpCopy = tump
    tump = o
    o += tumpCopy
    # print(Fibs)
    count += 1

    if Max < tump:
        break
        
Fibs = Fibs[::-1]
# print(Fibs)

for i in range(n):
    x = num[i]
    str = ""

    for j in range(count):
        if Fibs[j] <= x:
            x = x - Fibs[j]
            str = str + "1"

        elif Fibs[j] <= num[i]:
            str = str + "0"

        else:
            continue

    print(num[i], "=", str, "(fib)")