is_87 = True
is_sb = True

Q1 = input("is_sb(yes or no):")
if Q1 == 'no':
    is_sb = False

Q2 = input("is_87(yes or no):")

if Q2 == 'no':
    is_87 = False

if is_sb == is_87 == True:
    print("you are a 87 and a sb")
elif is_87:
    print("you are a 87")
elif is_sb:
    print("you are a sb")
else:
    print("you are neither a 87 nor a sb")