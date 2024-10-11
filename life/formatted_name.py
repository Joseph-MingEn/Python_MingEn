# 定義一個包含逗號的字串
# name = "TU,MING-EN"
name = input("這是input:")

# 使用 find() 方法找到逗號的位置
comma_index = name.find(',')

# 使用切片來分割字串
part1 = name[:comma_index]
part2 = name[comma_index + 1:]

# 輸出結果
print(part2, part1)