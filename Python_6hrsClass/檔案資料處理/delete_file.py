import os

path = r"C:\Users\TUMINGEN\Documents\GitHub\pymingen\Python_6hrsClass\檔案資料處理"
# 刪除檔案
# try:
#     os.remove(f"{path}/copied_file.txt")
# except FileNotFoundError:
#     print("File not found")

# 刪除空資料夾
# try:
#     os.rmdir(f"{path}/space_dirc")
# except FileNotFoundError:
#     print("Space_dirc not found")

# 刪除有文件的資料夾
# try:
#     os.rmtree(f"{path}/Dirc")
# except FileNotFoundError:
#     print("Dirc not found")

# 丟到資源回收桶
import send2trash
try:
    send2trash.send2trash(fr"{path}\copied_file.txt")
except FileNotFoundError:
    print("File not found")