name = input("Enter your name:")

while name == "":
    print("Please enter a valid name.")
    name = input("Enter your name:")

print(f"Hello, {name}!")
