import pygame
import random
import sys
import os

# 初始化 Pygame
pygame.init()

# 設定視窗
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('簡易貪吃蛇')

# 顏色設定
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# 方塊大小
block_size = 20

# 改進的圖片載入函數
def load_image(path):
    if not os.path.exists(path):
        print(f"Error: File '{path}' not found.")
        sys.exit()
    return pygame.image.load(path)

# 載入圖片
snake_head_img = load_image("pygame\\head_0.png")
snake_body_img = load_image("pygame\\body_0.png")
food_img = load_image("pygame\\food_0.png")
bad_food_img = load_image("pygame\\bad_food_0.png")

# 調整圖片大小
snake_head_img = pygame.transform.scale(snake_head_img, (block_size, block_size))
snake_body_img = pygame.transform.scale(snake_body_img, (block_size, block_size))
food_img = pygame.transform.scale(food_img, (block_size, block_size))
bad_food_img = pygame.transform.scale(bad_food_img, (block_size, block_size))

# 設定蛇的初始位置
snake_pos = [(100, 100), (90, 100), (80, 100)]
snake_direction = 'RIGHT'
change_to = snake_direction

# 設定食物和壞食物的位置
food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
            random.randrange(1, (screen_height // block_size)) * block_size)
bad_food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
                random.randrange(1, (screen_height // block_size)) * block_size)
food_spawn = True
bad_food_spawn = True

# 設定遊戲速度
clock = pygame.time.Clock()
snake_speed = 15

# 設定初始分數
score = 0

# 顯示遊戲結束訊息和分數
font_style = pygame.font.SysFont("SimHei", 25)
score_font = pygame.font.SysFont("SimHei", 35)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def show_score(color, font, size):
    score_surface = font.render(f"Score : {score}", True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (screen_width / 2, 10)
    screen.blit(score_surface, score_rect)

def game_menu():
    while True:
        screen.fill(WHITE)
        menu_font = pygame.font.SysFont("SimHei", 50)
        menu_surface = menu_font.render("Snake", True, BLACK)
        start_surface = menu_font.render("GameStart", True, BLACK)
        quit_surface = menu_font.render("End", True, BLACK)

        start_rect = start_surface.get_rect(center=(screen_width / 2, screen_height / 2))
        quit_rect = quit_surface.get_rect(center=(screen_width / 2, screen_height / 1.5))

        screen.blit(menu_surface, (screen_width / 2 - menu_surface.get_width() / 2, screen_height / 4))
        screen.blit(start_surface, start_rect)
        screen.blit(quit_surface, quit_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # 開始遊戲
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    return  # 開始遊戲
                if quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global snake_pos, snake_direction, change_to, food_pos, food_spawn, bad_food_pos, bad_food_spawn, score

    snake_pos = [(100, 100), (90, 100), (80, 100)]
    snake_direction = 'RIGHT'
    change_to = snake_direction
    food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
                random.randrange(1, (screen_height // block_size)) * block_size)
    bad_food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
                    random.randrange(1, (screen_height // block_size)) * block_size)
    food_spawn = True
    bad_food_spawn = True
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 監聽鍵盤事件來控制蛇的移動
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'

        # 確保蛇不會反向
        if change_to == 'LEFT' and snake_direction != 'RIGHT':
            snake_direction = 'LEFT'
        if change_to == 'RIGHT' and snake_direction != 'LEFT':
            snake_direction = 'RIGHT'
        if change_to == 'UP' and snake_direction != 'DOWN':
            snake_direction = 'UP'
        if change_to == 'DOWN' and snake_direction != 'UP':
            snake_direction = 'DOWN'

        # 更新蛇的位置
        if snake_direction == 'LEFT':
            new_head = (snake_pos[0][0] - block_size, snake_pos[0][1])
        if snake_direction == 'RIGHT':
            new_head = (snake_pos[0][0] + block_size, snake_pos[0][1])
        if snake_direction == 'UP':
            new_head = (snake_pos[0][0], snake_pos[0][1] - block_size)
        if snake_direction == 'DOWN':
            new_head = (snake_pos[0][0], snake_pos[0][1] + block_size)

        # 檢查是否出界
        if new_head[0] < 0 or new_head[0] >= screen_width or new_head[1] < 0 or new_head[1] >= screen_height:
            message("Game Over! Out of Bounds.", RED)
            pygame.display.update()
            pygame.time.wait(2000)
            return

        # 如果蛇吃到食物
        snake_pos.insert(0, new_head)
        if snake_pos[0] == food_pos:
            food_spawn = False
            bad_food_spawn = False
            score += 1
        elif snake_pos[0] == bad_food_pos:
            bad_food_spawn = False
            message("Game over! Eating Bad Food", BLACK)
            pygame.display.update()
            pygame.time.wait(2000)
            return
        else:
            snake_pos.pop()

        # 生成新的食物
        if not food_spawn:
            food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
                        random.randrange(1, (screen_height // block_size)) * block_size)
        food_spawn = True

        # 生成新的壞食物
        if not bad_food_spawn:
            bad_food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
                            random.randrange(1, (screen_height // block_size)) * block_size)
        bad_food_spawn = True

        # 填充背景顏色
        screen.fill(WHITE)

        # 畫出網格
        for x in range(0, screen_width, block_size):
            pygame.draw.line(screen, GRAY, (x, 0), (x, screen_height))
        for y in range(0, screen_height, block_size):
            pygame.draw.line(screen, GRAY, (0, y), (screen_width, y))

        # 畫出蛇（使用圖片）
        screen.blit(snake_head_img, (snake_pos[0][0], snake_pos[0][1]))
        for segment in snake_pos[1:]:
            screen.blit(snake_body_img, (segment[0], segment[1]))

        # 畫出食物（使用圖片）
        screen.blit(food_img, (food_pos[0], food_pos[1]))
        screen.blit(bad_food_img, (bad_food_pos[0], bad_food_pos[1]))

        # 顯示分數
        show_score(BLACK, score_font, 35)

        pygame.display.update()
        clock.tick(snake_speed)

# 主程式流程
game_menu()
game_loop()