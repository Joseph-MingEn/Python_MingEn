import os

# 檢測檔案是否存在
str = r"C:\Users\TUMINGEN\Documents\GitHub\pymingen\Python_6hrsClass\檔案資料處理\file_detect.py"
print(str)
if os.path.exists(str):
    print("File exist")
else:
    print("File does not exist")

# 檢測是否為檔案
if os.path.isfile(str):
    print("It's a file")
elif os.path.isdir(str):
    print("It's a directory")
else:
    print("other")