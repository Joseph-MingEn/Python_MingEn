str = r"C:\Users\TUMINGEN\Documents\GitHub\pymingen\Python_6hrsClass\檔案資料處理\read_file.py"
try:
    with open(str) as file:
        print(file.read())
except FileExistsError:
    print("File does not exist")