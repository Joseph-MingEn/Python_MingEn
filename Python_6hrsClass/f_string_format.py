number1 = 123.11111
number2 = 3456.12
number3 = -12.2222

#控制小數點
print(f"number1:{number1:.2f}\n"
      f"number2:{number2:.2f}\n"
      f"number3:{number3:.2f}")

#加正負號
print("\n")
print(f"number1:{number1:+.2f}\n"
      f"number2:{number2:+.2f}\n"
      f"number3:{number3:+.2f}")

#對齊 < > ^

print(">")
print(f"number1:{number1:>10.2f}\n"
      f"number2:{number2:>10.2f}\n"
      f"number3:{number3:>10.2f}")

print("<")
print(f"number1:{number1:<10.2f}\n"
      f"number2:{number2:<10.2f}\n"
      f"number3:{number3:<10.2f}")

print("^")
print(f"number1:{number1:^10.2f}\n"
      f"number2:{number2:^10.2f}\n"
      f"number3:{number3:^10.2f}")