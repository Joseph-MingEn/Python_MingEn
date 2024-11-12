# 鍵 => 值
# key => value

capital = {
    "USA": "Washington D.C.",
    "UK": "London",
    "Canada": "Ottawa",
    "Japan": "Tokyo",
    "China": "Beijing"
}

#get()
print(capital.get("USA"))

#update()
capital.update({"Taiwan" : "Taipei"})
print(capital)

#pop()
capital.pop("China")
print(capital)

#values()
print(capital.values())

#items()
print(capital.items())