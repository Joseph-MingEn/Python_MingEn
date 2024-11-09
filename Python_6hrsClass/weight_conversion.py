weight = float(input("Please enter your wight: "))

unit = input("Unit(kg or lb): ")

translations = input("To change unit: ")

if unit == "kg":
    if translations == "kg":
        weight_in_kg = weight
        weight_in_kg = round(weight_in_kg, 2)
        print(f"Your weight is {weight_in_kg} kg.")
    elif translations == "lb":
        weight_in_lbs = weight * 2.20462
        weight_in_lbs = round(weight_in_lbs, 2)
        print(f"Your weight is {weight_in_lbs} lb.")
    else:
        print("Invalid unit.")
elif unit == "lb":
    if translations == "kg":
        weight_in_kg = weight / 2.20462
        weight_in_kg = round(weight_in_kg, 2)
        print(f"Your weight is {weight_in_kg} kg.")
    elif translations == "lb":
        weight_in_lbs = weight
        weight_in_lbs = round(weight_in_lbs, 2)
        print(f"Your weight is {weight_in_lbs} lb.")
    else:
        print("Invalid unit.")
else:
    print("Invalid unit.")

print("Your are thin...")