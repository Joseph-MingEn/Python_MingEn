a,b = map(int, input().split())
guest = int(input())
total = 0
for i in range(guest):
    good_list = [int(x) for x in input().split()]

    A = good_list.count(a) - good_list.count(-a)
    B = good_list.count(b) - good_list.count(-b)
    # print(A, B)
    if A > 0 and B > 0:
        total += 1
        # print(total)

print(total)

print(good_list[0])