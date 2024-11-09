credit_card = "1234-5678-9876-5432"
for x in credit_card:
    print(x)

print("continue")

for x in credit_card:
    if x == "9":
        continue
    else:
        print(x)

print("break")

for x in credit_card:
    if x == "9":
        break
    else:
        print(x)

print("dictionary")

my_dict = {"a" : "1", "b" : "2", "c" : "3"}

for x in my_dict:
    print(x)

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")