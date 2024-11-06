#顯示type
name = "Joseph"
age = 18
gpa = 0.0001
is_boy = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_boy))

print('\n')

#顯式type轉換
is_boy = str(is_boy)
print(is_boy)
print(type(is_boy))

print('\n')

#隱式type轉換
x = 10
y = 2
print(type(x))
x = x/y
print(x)
print(type(x))