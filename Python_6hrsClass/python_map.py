# map

#map(函數, 可跌代的東西)

store = [
    ("Dog", 10),
    ("Cat", 15),
    ("Rabbit", 5),
    ("Bird", 2)
]

to_usd = lambda list : (list[0], list[1] * 40)

print(map(to_usd, store))

print(list(map(to_usd, store)))

to_twd = lambda list : (list[0], list[1] * 120)

print(list(map(to_twd, store)))