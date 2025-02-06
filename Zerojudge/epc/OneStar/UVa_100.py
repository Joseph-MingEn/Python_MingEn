# 記憶化字典
memo = {}

def collatz_length(n):
    if n in memo:
        return memo[n]
    
    original_n = n
    length = 1
    while n != 1:
        if n in memo:
            length += memo[n] - 1
            break
        elif n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        length += 1
    memo[original_n] = length
    return length

while True:
    try:
        user_input = input("")

        i, j = map(int, user_input.split())
        Max = 0

        if i > j:
            for x in range(j, i + 1):
                length = collatz_length(x)
                Max = max(Max, length)
        else:
            for x in range(i, j + 1):
                length = collatz_length(x)
                Max = max(Max, length)

        print(f"{i} {j} {Max}")

    except EOFError:
            break