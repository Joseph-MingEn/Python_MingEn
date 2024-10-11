import pygame
import os
import time

pygame.init()
screen = pygame.display.set_mode((810, 456))
pygame.display.set_caption('翻頁時鐘')

# 加載並放大GIF每一幀圖片
frame_folder = 'C:\\Users\\TUMINGEN\\Documents\\GitHub\\pymingen\\life\\frames'
frames = [pygame.image.load(os.path.join(frame_folder, f)) for f in os.listdir(frame_folder)]
frames = [pygame.transform.smoothscale(f, (int(f.get_width() * 1.5), int(f.get_height() * 1.5))) for f in frames]
frame_index = 0

# 確保系統有該字體，指定字體文件路徑
font_path = "C:\\Users\\TUMINGEN\\Documents\\字體\\OneDrive-2024-10-10\\Zip 形式でダウンロード\\genjyuugothic-x-20150607\\GenJyuuGothicX-Monospace-Bold.ttf"  # 根據你的操作系統路徑進行修改
font_time = pygame.font.Font(font_path, 60)  # 原120的一半
font_date = pygame.font.Font(font_path, 25)  # 原50的一半
font_quote = pygame.font.Font(font_path, 18)  # 原36的一半

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    
    # 顯示背景的下一幀
    screen.blit(frames[frame_index], (0, 0))
    frame_index = (frame_index + 1) % len(frames)

    # 獲取當前時間和日期
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%Y年%m月%d日 %A")
    quote = "明天的事交給明天去做"

    # 渲染文字
    img_time = font_time.render(current_time, True, (255, 255, 255), (50, 50, 50))
    img_date = font_date.render(current_date, True, (255, 255, 255))
    img_quote = font_quote.render(quote, True, (255, 255, 255))
    
    # 計算時間的位置
    time_position = (screen.get_width() - img_time.get_width() - 10, screen.get_height() - img_time.get_height() - 10)
    date_position = (screen.get_width() - img_date.get_width() - 10, time_position[1] - img_date.get_height() - 10)
    quote_position = (screen.get_width() - img_quote.get_width() - 10, date_position[1] - img_quote.get_height() - 10)
    
    # 顯示文字
    screen.blit(img_time, time_position)
    screen.blit(img_date, date_position)
    screen.blit(img_quote, quote_position)
    
    pygame.display.update()
    time.sleep(0.1)  # 每幀間隔時間，根據需要調整
    
pygame.quit()
