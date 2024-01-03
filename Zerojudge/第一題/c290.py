X = str(input())
#print(X)
A = B = 0

for i in range(len(X)):
    if i%2 != 0:
        A += int(X[i])
    else:
        B += int(X[i])


print(abs(A-B))