name = "joseph 涂名恩"

lenght = len(name)
print(name + "一共有" + str(lenght) + "個字元")

space_pso = name.find("h")
print("第一個h出現在", space_pso, "個字元")

name_capitalized = name.capitalize()
print("第一字轉為大寫", name_capitalized)

name_upper = name.upper()
print("全部轉為大寫", name_upper)

name_lower = name.lower()
print("全部轉為小寫", name_lower)

phone_number = input("Phone Number: ")
phone_number_couunt = phone_number.count("-")
print("電話號碼有", phone_number_couunt, "個-字號")

phone_number_replace = phone_number.replace("-", " ")
print("phone number: ", phone_number_replace)

# 程式練習
# 1. Username don't over 12 strings
# 2. Username cannot contain spaces and numbers
# 3. If they all match, show "歡迎 + User Name"

name = input("Please enter your Username: ")
is_pass = True

if name.count(" ") > 0:
    print("Username cannot contain spaces")
    is_pass = False
if len(name) > 12:
    print("Username don't over 12 strings")
    is_pass = False
    
# for i in range(10):
#     if name.count(str(i)) > 0:
#         print("Username cannot contain numbers")
#         is_pass = False
#         break

#isalpha() 偵測是否有除英文以外的字元
if not name.isalpha():
    print("Username cannot contain numbers")
    is_pass = False

if is_pass == True:
    print("歡迎", name)