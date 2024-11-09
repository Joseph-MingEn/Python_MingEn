for x in range(1, 10):
    print(x, end=" ")
print("\n", "5 * 9")
for y in range(5):
    for x in range(1, 10):
        print(x, end=" ")
    print()

rows = int(input("enter the number of rows:"))
cols = int(input("enter the number of columns:"))
symbol = input("enter the symbol:")

for i in range(rows):
    for j in range(cols):
        print(symbol, end=" ")
    print()
