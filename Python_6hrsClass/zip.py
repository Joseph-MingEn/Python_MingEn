# Zip function

usernames = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
passwords = ["123", "456", "789", "000", "111"]
dates = ["123-12-12", "123-12-14", "123-12-16", "123-12-17", "123-12-18"]
users = zip(usernames, passwords, dates)
print(users)

# Unzip只可以用一次
for i in users:
    print(i)

print(list(users))

# user_dict = dict(users)
# print(user_dict)

# # 三個以上就不可以用
# for key, value in user_dict.items():
#     print(f"Username: {key}, Password: {value}")