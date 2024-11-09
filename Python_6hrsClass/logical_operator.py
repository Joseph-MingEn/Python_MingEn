ago = int(input("How old are you?"))

if ago < 0 & ago < 3:
    print("You are a baby.")
elif ago < 3 & ago < 12:
    print("You are a kid.")
elif ago < 12 & ago < 20:
    print("You are a teenager.")
elif ago < 20 & ago < 65:
    print("You are an adult.")
elif ago < 65 & ago < 90:
    print("You are a senior citizen.")
elif ago < 0 | ago > 120:
    print("... cool")