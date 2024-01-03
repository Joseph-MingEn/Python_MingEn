# 輸入格式：每一行的數字用空格分隔，不同行用換行符號分隔
# 例如：
# 1 2 3
# 4 5 6
# 7 8 9

# 讀取二維陣列
rows, cols = map(int, input("請輸入行和列的數量（空格分隔）：").split())

# 使用列表生成式讀取二維陣列
matrix = [list(map(int, input().split())) for _ in range(rows)]

# 輸出二維陣列
print("輸入的二維陣列：")
for row in matrix:
    print(row)  

#%%
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

for i in A :
    print(i)

#%%
n = int(input("請輸入行數："))

# 使用列表生成式讀取二維陣列（兩列）
A = [list(map(int, input().split())) for _ in range(n)]

# 輸出二維陣列
print("輸入的二維陣列：")
for row in A:
    print(row)
# %%
