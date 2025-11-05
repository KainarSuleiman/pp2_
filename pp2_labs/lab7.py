# import pygame, datetime, math, sys
#
# pygame.init()
# WIDTH, HEIGHT = 800, 800
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Mickey Clock")
#
# clock = pygame.time.Clock()
#
# # --- Загружаем изображения ---
# body = pygame.image.load("mickey_body.png").convert_alpha()
# right_hand = pygame.image.load("right_hand.png").convert_alpha()  # минутная
# left_hand = pygame.image.load("left_hand.png").convert_alpha()    # секундная
#
# body = pygame.transform.scale(body, (800, 800))
# right_hand = pygame.transform.scale(right_hand, (300, 100))
# left_hand = pygame.transform.scale(left_hand, (300, 100))
#
# CENTER = (WIDTH // 2, HEIGHT // 2)
#
# def blit_rotate_center(surface, image, top_left, angle):
#     """Функция поворота картинки вокруг центра"""
#     rotated_image = pygame.transform.rotate(image, angle)
#     new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
#     surface.blit(rotated_image, new_rect.topleft)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     now = datetime.datetime.now()
#     minute = now.minute
#     second = now.second
#
#     minute_angle = -(minute * 6)
#     second_angle = -(second * 6)
#
#     screen.fill((255, 255, 255))
#     screen.blit(body, (0, 0))
#
#     # Рисуем руки (поворачиваем)
#     blit_rotate_center(screen, right_hand, (CENTER[0] - 150, CENTER[1] - 50), minute_angle)
#     blit_rotate_center(screen, left_hand, (CENTER[0] - 150, CENTER[1] - 50), second_angle)
#
#     pygame.display.update()
#     clock.tick(30)

#
# import pygame
# import sys
#
# pygame.init()
#
# # --- Настройки окна ---
# screen = pygame.display.set_mode((500, 300))
# pygame.display.set_caption("Радио пп2")
#
# # --- Инициализация звука ---
# pygame.mixer.init()
#
# # --- Плейлист ---
# songs = ["Ernar Amandyq - Meni kut.mp3", "Ваграм Вазян - Любовь и Боль.mp3", "Кайрат Нуртас - Мейли.mp3"]  # твои файлы
# current = 0
# is_playing = False
#
# def play_song():
#     global is_playing
#     pygame.mixer.music.load(songs[current])
#     pygame.mixer.music.play()
#     is_playing = True
#     print(f"▶️ Playing: {songs[current]}")
#
# def stop_song():
#     global is_playing
#     pygame.mixer.music.stop()
#     is_playing = False
#     print("⏹ Stopped")
#
# def next_song():
#     global current
#     current = (current + 1) % len(songs)
#     play_song()
#
# def prev_song():
#     global current
#     current = (current - 1) % len(songs)
#     play_song()
#
# font = pygame.font.SysFont(None, 36)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_p:  # play
#                 play_song()
#             elif event.key == pygame.K_s:  # stop
#                 stop_song()
#             elif event.key == pygame.K_n:  # next
#                 next_song()
#             elif event.key == pygame.K_b:  # previous
#                 prev_song()
#
#     screen.fill((255, 255, 255))
#     text = font.render(f"Now playing: {songs[current]}", True, (0, 0, 0))
#     screen.blit(text, (50, 130))
#
#     pygame.display.update()
#


import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Красный пп-шный шарик")


color = (255, 0, 0)
x = WIDTH // 2
y = HEIGHT // 2
radius = 25
speed = 20


clock = pygame.time.Clock()

while True:
    for deistvie in pygame.event.get():
        if deistvie.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if deistvie.type == pygame.KEYDOWN:
            if deistvie.key == pygame.K_UP and y - radius - speed >= 0:
                y -= speed
            elif deistvie.key == pygame.K_DOWN and y + radius + speed <= HEIGHT:
                y += speed
            elif deistvie.key == pygame.K_LEFT and x - radius - speed >= 0:
                x -= speed
            elif deistvie.key == pygame.K_RIGHT and x + radius + speed <= WIDTH:
                x += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.update()
    clock.tick(30)
