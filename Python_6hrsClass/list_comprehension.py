# 列表推導式(list comprehension)

# 列表推導式 => 更少的語法創建新列表

# EX1
# 一般
def square(x):
    return x * x

list = []

for i in range(1, 11):
    list.append(square(i))

print("一般 \n", list)
# 列表推導式
square = [i * i for i in range(1, 11)]

print("列表推導式 \n", square)

# EX2 過濾學生成績
grades = [10, 20, 30, 40, 50, 60, 70, 80]

pass_grades = [i for i in grades if i >= 60]

print(pass_grades)