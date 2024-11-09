temp = float(input("Please enter temperature now(pure numbers!!!): "))
now_unit = input("Please enter unit(C, F, K): ")
translations = input("Please enter translations unit(C, F, K): ")

if now_unit == "C":
    if translations == "F":
        now_temp = temp * 9 / 5 + 32
        print(f"Temperature is {now_temp:.1f} F.")
    elif translations == "K":
        now_temp = temp + 273.15
        print(f"Temperature is {now_temp:.1f} K.")
    else:
        print("Invalid unit.")
elif now_unit == "F":
    if translations == "C":
        now_temp = (temp - 32) * 5 / 9
        print(f"Temperature is {now_temp:.1f} C.")
    elif translations == "K":
        now_temp = (temp - 32) * 5 / 9 + 273.15
        print(f"Temperature is {now_temp:.1f} K.")
    else:
        print("Invalid unit.")
elif now_unit == "K":
    if translations == "C":
        now_temp = temp - 273.15
        print(f"Temperature is {now_temp:.1f} C.")
    elif translations == "F":
        now_temp = temp * 9 / 5 - 459.67
        print(f"Temperature is {now_temp:.1f} F.")
    else:
        print("Invalid unit.")
else:
    print("Invalid unit.")

print("It is hot!!!")