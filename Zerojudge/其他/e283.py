#%%
try:
    while True:
        n = int(input())
        ans = ""
        for i in range(n):
            a, b, c, d = map(int, input().split())
            num = [a, b, c, d]
            if num == [0, 1, 0, 1]:
                ans += "A"
            elif num == [0, 1, 1, 1]:
                ans += "B"
            elif num == [0, 0, 1, 0]:
                ans += "C"
            elif num == [1, 1, 0, 1]:
                ans += "D"
            elif num == [1, 0, 0, 0]:
                ans += "E"
            elif num == [1, 1, 0, 0]:
                ans += "F"

        print(ans)
except EOFError:
    pass
#%%
try:
    while True:
        my_dict = {101: "A", 111: "B", 10: "C", 1101: "D", 1000: "E", 1100: "F"}
        n = int(input())
        ans = ""
        for i in range(n):
            a, b, c, d = map(int, input().split())
            ans += my_dict[1000*a + 100*b + 10*c + d]

        print(ans)
except EOFError:
    pass
# %%
try:
    while True:
        my_dict = {101: "A", 111: "B", 10: "C", 1101: "D", 1000: "E", 1100: "F"}
        n = int(input())
        ans = []
        for i in range(n):
            a, b, c, d = map(int, input().split())
            ans.append(my_dict[1000*a + 100*b + 10*c + d])

        result = ''.join(ans)
        print(result)
except EOFError:
    pass
# %%
import sys
letter = {"0 1 0 1": "A",
          "0 1 1 1": "B",
          "0 0 1 0": "C",
          "1 1 0 1": "D",
          "1 0 0 0": "E",
          "1 1 0 0": "F"}
 
for i in sys.stdin:
    n = int(i)
    ans = ""
    for i in range(n):
        s = sys.stdin.readline().strip()
        ans += letter[s]
    print (ans)