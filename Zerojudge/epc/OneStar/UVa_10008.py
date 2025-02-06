n = int(input())

ans = {}
Max = 0
for i in range(n):
    s = str(input())
    for index, char in enumerate(s):
        for j in range(26):
            c1 = j + 65
            c2 = j + 97
            if char == str(chr(c1)) or char == str(chr(c2)):
                if c1 in ans:
                    ans[c1] += 1
                    Max = max(Max, ans[c1])
                else:
                    ans.update({c1 : 1})
                # print(ans)
                continue

# print(Max)

# print(sorted(ans.items()))

for i in range(Max):
    x = Max - i
    for key, value in ans.items():
        if x == value:
            print(chr(key), x)