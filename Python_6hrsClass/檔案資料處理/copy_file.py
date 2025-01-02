import shutil
# - copyfile 只會複製文件內容不會複製描述資訊(如:建立日期...)
# - copy 跟copyfile一樣但它還可以複製目錄
# - copy2 可以複製文件內容以及複製描述資訊
str = r"C:\Users\TUMINGEN\Documents\GitHub\pymingen\Python_6hrsClass"
source = f"{str}/oop.py"
destination = f"{str}/oop_class_variable.py"
shutil.copyfile(source, destination)