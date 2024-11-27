import pygame
import random
import sys

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

# 方塊大小
block_size = 20

# 設定蛇的初始位置
snake_pos = [(100, 100), (90, 100), (80, 100)]
snake_direction = 'RIGHT'
change_to = snake_direction

# 設定食物的位置
food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
            random.randrange(1, (screen_height // block_size)) * block_size)
food_spawn = True

bad_food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
            random.randrange(1, (screen_height // block_size)) * block_size)
bad_food_spawn = True

# 設定遊戲速度
clock = pygame.time.Clock()
snake_speed = 15

# 顯示遊戲結束訊息
font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# 遊戲主迴圈
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

    # 如果蛇吃到食物
    snake_pos.insert(0, new_head)
    if snake_pos[0] == food_pos:
        food_spawn = False
        bad_food_spawn = False
    elif snake_pos[0] == bad_food_pos:
        bad_food_spawn = False
    else:
        snake_pos.pop()

    # 生成新的食物
    if not food_spawn:
        food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
                    random.randrange(1, (screen_height // block_size)) * block_size)
    food_spawn = True

    if not bad_food_spawn:
        bad_food_pos = (random.randrange(1, (screen_width // block_size)) * block_size,
                    random.randrange(1, (screen_height // block_size)) * block_size)
    bad_food_spawn = True

    # 填充背景顏色
    screen.fill(WHITE)

    # 畫出蛇
    for segment in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], block_size, block_size))

    # 畫出食物
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))
    pygame.draw.rect(screen, BLACK, pygame.Rect(bad_food_pos[0], bad_food_pos[1], block_size, block_size))

    # 檢查是否撞到邊界或自己
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or
        snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height):
        message("遊戲結束! 撞到邊界", BLACK)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            message("遊戲結束! 撞到自己", BLACK)
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

    # 更新顯示
    pygame.display.update()

    # 設定遊戲速度
    clock.tick(snake_speed)
