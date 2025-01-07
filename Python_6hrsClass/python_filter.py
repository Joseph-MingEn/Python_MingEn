# filter 過濾

#可用來過濾可跌代的資料結構(list, ...)

friends = [
    ("John", 20),
    ("Bob", 12),
    ("Steven", 18),
    ("Alice", 22),
    ("Eve", 16)
]

age_filter = lambda list : list[1] >= 18

can_drink_friends = list(filter(age_filter, friends))

for friend in can_drink_friends:
    print(f"{friend[0]} is {friend[1]} years old and can drink.")