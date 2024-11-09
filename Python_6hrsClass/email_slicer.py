email = "42th214@gmail.com"

#index("X") 可以知道第一個"X"是在字串的哪裡
index = email.index("@")
print(index)

print("email:", email[:index])
print("email 網域:",email[index+1:])