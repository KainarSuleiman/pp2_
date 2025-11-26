# #
# # import pygame
# # import math
# # import datetime
# #
# # pygame.init()
# #
# # # Размер окна
# # WIDTH, HEIGHT = 600, 600
# # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption("Mickey Clock")
# #
# # clock = pygame.time.Clock()
# #
# # mickey = pygame.image.load("mickey.png").convert_alpha()
# # mickey = pygame.transform.smoothscale(mickey, (500, 500))  # уменьшаем при необходимости
# # center = (WIDTH // 2, HEIGHT // 2)
# #
# # def draw_hand(surface, center, length, angle_deg, color, width):
# #
# #     angle_rad = math.radians(angle_deg - 90)
# #     end_x = center[0] + length * math.cos(angle_rad)
# #     end_y = center[1] + length * math.sin(angle_rad)
# #     pygame.draw.line(surface, color, center, (end_x, end_y), width)
# #
# # running = True
# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #
# #     screen.fill((255, 255, 255))
# #     screen.blit(mickey, mickey.get_rect(center=center))
# #
# #     # Получаем текущее время
# #     now = datetime.datetime.now()
# #     minute_angle = 6 * now.minute         # 360° / 60 = 6°
# #     second_angle = 6 * now.second
# #
# #
# #
# #     draw_hand(screen, center, 160, minute_angle, (0, 0, 0), 8)
# #
# #
# #     draw_hand(screen, center, 175, second_angle, (255, 0, 0), 4)
# #
# #     pygame.display.flip()
# #     clock.tick(30)
# #
# # pygame.quit()
#
# import pygame
#
# pygame.init()
#
# screen = pygame.display.set_mode((700, 300))
# pygame.display.set_caption("Радио пп2")
#
# pygame.mixer.init()
#
# songs = ["Ernar Amandyq - Meni kut.mp3", "Ваграм Вазян - Любовь и Боль.mp3", "Кайрат Нуртас - Мейли.mp3"]
# current = 0
# is_playing = False
#
# def play_song():
#     global is_playing
#     pygame.mixer.music.load(songs[current])
#     pygame.mixer.music.play()
#     is_playing = True
#     print(f" Playing: {songs[current]}")
#
# def stop_song():
#     global is_playing
#     pygame.mixer.music.stop()
#     is_playing = False
#     print(" Stopped")
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
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_p:
#                 play_song()
#             elif event.key == pygame.K_s:
#                 stop_song()
#             elif event.key == pygame.K_n:
#                 next_song()
#             elif event.key == pygame.K_b:
#                 prev_song()
#
#     screen.fill((255, 255, 255))
#     text = font.render(f"Now playing: {songs[current]}", True, (0, 0, 0))
#     screen.blit(text, (50, 130))
#
#     pygame.display.update()
#
# pygame.quit()

import pygame

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
running = True

while running:
    for deistvie in pygame.event.get():
        if deistvie.type == pygame.QUIT:
            running = False

        if deistvie.type == pygame.KEYDOWN:
            if deistvie.key == pygame.K_UP and y - radius  >= 0:
                y -= speed
            elif deistvie.key == pygame.K_DOWN and y + radius  <= HEIGHT:
                y += speed
            elif deistvie.key == pygame.K_LEFT and x - radius >= 0:
                x -= speed
            elif deistvie.key == pygame.K_RIGHT and x + radius <= WIDTH:
                x += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
