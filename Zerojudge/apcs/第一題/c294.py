a, b, c = map(int, input().split())
L = [a, b, c]
L.sort()

print(*L)
if L[0] + L[1] < L[2]:
    print("No")
elif L[0]**2 + L[1]**2 < L[2]**2:
    print("Obtuse")
elif L[0]**2 + L[1]**2 == L[2]**2:
    print("Right")
elif L[0]**2 + L[1]**2 > L[2]**2:
    print("Acute")