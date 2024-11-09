# original_money = floot(input("Enter your amount:"))
# rate = floot(input("Rate:"))
# time = floot(input("Time:"))
# total = floot(0)

# total = original_money * (1 + (rate / 100)) ** time

amount = 0
while amount <= 0:
    amount = float(input("Enter your amount:"))

    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")

rate = 0
while rate <= 0:
    rate = float(input("Enter your rate:"))

    if rate <= 0:
        print("Invalid rate. Please enter a positive number.")

time = 0
while time <= 0:
    time = float(input("Enter your rate:"))

    if time <= 0:
        print("Invalid time. Please enter a positive number.")

total = float(0)

total = amount * (1 + (rate / 100)) ** time

print("The total amount after", time, "years is:", total)