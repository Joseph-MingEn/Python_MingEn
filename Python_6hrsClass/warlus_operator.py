#獠牙運算符(賦值表達式) :=

#EX1
#一般
happy = True
print(happy)

#:=
print(happy := False)

#EX2
#一般
foods = []

while True:
    food = input("What is your favorite food?")
    if food == "quit":
        break
    foods.append(food)

print(foods)

print("換 := ")
del foods #清除變數

#:=

foods = []

while (food := input("What is your favorite food?")) != "quit":
    foods.append(food)

print(foods)