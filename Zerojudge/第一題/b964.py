n = int(input())
#print(n)

G = list(map(int,input().split()))
G.sort()
print(*G)

b = w = -1

for i in range(n):
    if (G[i] < 60) & (G[i] > b):
        b = G[i]

for i in range(n):
    if G[i] >= 60:
        w = G[i]
        break

if b == -1:
    print("best case")
else :
    print(b)

if w == -1:
    print("worst case")
else :
    print(w)