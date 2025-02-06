n, m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]
ax = []
ay = []
count = 0
'''
for i in MAP:
    print(i)
'''
for i in range(n):
    for j in range(m):
        x = MAP[i][j]
        total = 0

        for s in range(i-x, i+x+1):
            for t in range(j-x, j+x+1):
                if 0 <= s < n and 0 <= t < m and abs(i-s) + abs(j-t) <= x:
                    total += MAP[s][t]

        if (total-x) % 10 == 0:
            count += 1
            ax.append(i)
            ay.append(j)

print(count)
for i in range(count):
    print(ax[i],ay[i])