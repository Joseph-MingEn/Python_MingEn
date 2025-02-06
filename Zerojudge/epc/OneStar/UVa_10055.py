import sys

input = sys.stdin.read

data = list(map(int, input().split()))
i = 0
while i < len(data):
    print(abs(data[i] - data[i + 1]))
    i += 2