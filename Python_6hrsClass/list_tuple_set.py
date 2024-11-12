#list 列表
numbers = [1, 2, 3, 4, 5]

print(numbers[1])

for f in numbers:
    print(f)

#append 新增物件
numbers.append(2)
print(numbers)

#remove 去除物件
numbers.remove(3)
print(numbers)

#index 尋找第一個特定物件
print(numbers.index(2))

#count 輸出有幾個特定物件
print(numbers.count(2))

#sort 由小到大排序
numbers.sort()
print(numbers)

#reverse 反轉列表順序
numbers.reverse()
print(numbers)

#set

my_set = {"🐒", "🐩", "💔", "👩‍❤️‍👩", "🦷", "🥶"}#無法重複相同的物件
my_set.add("💀")
print(my_set)

if "💀"  in my_set:
    print("有一個💀")

#tuple 元組 無法事後更改元組中的物件
my_tuple = ("🐒", "🐩", "💔")
print(my_tuple[1])
print(my_tuple.count("🐒"))
print(my_tuple.index("🐒"))