n = int(input())

for i in range(n):
    Day = int(input())
    # Day_Relax = Day - 5
    Day_Relax = 6
    P = int(input())
    h = []
    Relax = []
    Day_h = []
    count_Relax = 0
    count_Day_h = 0

    # print("Day_Relax =", Day_Relax, "\nDay =", Day)
    
    while True:
        if Day_Relax <= Day:
            Relax.append(Day_Relax)
            count_Relax += 1
            Day_Relax += 1

        if Day_Relax <= Day:
            Relax.append(Day_Relax)
            count_Relax += 1
            Day_Relax += 6

        if Day_Relax > Day:
            break

    for j in range(P):
        h.append(int(input()))

        for k in range(Day // h[j]):
            Day_h.append(h[j] * (k + 1))
            count_Day_h += 1

    Day_h = sorted(Day_h)

    # print("Day_h.sorted =", Day_h, "\n")
    
    k = 1

    while True:
        if k == len(Day_h):
            break

        if Day_h[k-1] == Day_h[k]:
            Day_h[k-1] = 0
        k += 1

    # print("Day_h =", Day_h)
    Day_h = sorted(Day_h)
    
    for j in range(Day_h.count(0)):
        Day_h.remove(0)

    for j in range(len(Relax)):
        if Relax[j] in Day_h:
            Day_h.remove(Relax[j])
    
    # print("Day_h =", Day_h)

    print(len(Day_h))