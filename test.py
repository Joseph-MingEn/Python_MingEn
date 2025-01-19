try:
    while True:
        user_input = input("輸入一些內容，按下 Ctrl+D（在 UNIX/Linux 系統上）或 Ctrl+Z（在 Windows 系統上）結束: ")
        # 這裡可以處理輸入的內容
except EOFError:
    print("Hi")