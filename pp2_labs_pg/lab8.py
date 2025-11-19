#
# import sys
# import time
# import random
# import pygame
#
# # --- Initialization ---
# pygame.init()
#
# # --- Settings ---
# FPS = 60
# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 600
#
# # Начальная скорость, очки, монеты
# START_SPEED = 5
# SPEED_INCREASE_MS = 1000   # раз в 1 секунду увеличиваем скорость
#
# # --- Colors ---
# BLUE  = (0, 0, 255)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# # --- Asset paths (на случай, если захочешь потом поменять) ---
# BG_IMAGE_PATH     = "AnimatedStreet.png"
# PLAYER_IMAGE_PATH = "Player.png"
# ENEMY_IMAGE_PATH  = "Enemy.png"
# COIN_IMAGE_PATH   = "Coin.png"
# CRASH_SOUND_PATH  = "crash.wav"
# COIN_SOUND_PATH   = "coin.wav"
#
#
# # ============================
# # --- Classes ---
# # ============================
#
# class Enemy(pygame.sprite.Sprite):
#     """Вражеская машина, падает сверху вниз с заданной скоростью."""
#     def _init_(self):
#         super()._init_()
#         self.image = pygame.image.load(ENEMY_IMAGE_PATH).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.reset_position()
#
#     def reset_position(self):
#         """Выставляем врага наверх в случайную позицию по X."""
#         self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#
#     def update(self, speed: float):
#         """Двигаем врага вниз с учётом текущей скорости."""
#         self.rect.move_ip(0, speed)
#         if self.rect.top > SCREEN_HEIGHT:
#             self.reset_position()
#             return True  # враг прошёл экран → +1 очко
#         return False
#
#
# class Player(pygame.sprite.Sprite):
#     """Машина игрока, двигается влево-вправо по стрелкам."""
#     def _init_(self):
#         super()._init_()
#         self.image = pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.center = (160, 520)
#         self.speed_x = 5  # скорость по X
#
#     def update(self):
#         """Обрабатываем ввод и двигаем игрока."""
#         pressed_keys = pygame.key.get_pressed()
#
#         if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
#             self.rect.move_ip(-self.speed_x, 0)
#         if pressed_keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
#             self.rect.move_ip(self.speed_x, 0)
#
#
# class Coin(pygame.sprite.Sprite):
#     """Монета, падает сверху с меньшей скоростью, чем враг."""
#     def _init_(self):
#         super()._init_()
#         self.image = pygame.image.load(COIN_IMAGE_PATH).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.reset_position()
#
#     def reset_position(self):
#         """Сбрасываем монету наверх в новую случайную позицию."""
#         self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#
#     def update(self, speed: float):
#         """Двигаем монету вниз (чуть медленнее, чем враги)."""
#         self.rect.move_ip(0, speed * 0.5)
#         if self.rect.top > SCREEN_HEIGHT:
#             self.reset_position()
#
#
# # ============================
# # --- Main Game ---
# # ============================
#
# def main():
#     # --- Setup window, clock, fonts ---
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Racer (Improved)")
#
#     clock = pygame.time.Clock()
#
#     font_big = pygame.font.SysFont("Verdana", 60)
#     font_small = pygame.font.SysFont("Verdana", 20)
#     game_over_text = font_big.render("Game Over", True, BLACK)
#
#     # Фон
#     background = pygame.image.load(BG_IMAGE_PATH).convert()
#
#     # --- Game state ---
#     score = 0
#     coins = 0
#     speed = START_SPEED
#
#     # --- Sprites ---
#     player = Player()
#     enemy = Enemy()
#     coin = Coin()
#
#     enemies = pygame.sprite.Group(enemy)
#     coins_group = pygame.sprite.Group(coin)
#     all_sprites = pygame.sprite.Group(player, enemy, coin)
#
#     # --- Sounds (опционально: если файлов нет, просто не играем звуки) ---
#     try:
#         crash_sound = pygame.mixer.Sound(CRASH_SOUND_PATH)
#     except pygame.error:
#         crash_sound = None
#
#     try:
#         coin_sound = pygame.mixer.Sound(COIN_SOUND_PATH)
#     except pygame.error:
#         coin_sound = None
#
#     # --- Custom event: speed increase ---
#     INC_SPEED = pygame.USEREVENT + 1
#     pygame.time.set_timer(INC_SPEED, SPEED_INCREASE_MS)
#
#     running = True
#     while running:
#         # --- Event handling ---
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#             if event.type == INC_SPEED:
#                 speed += 0.5
#
#         # --- Update logic ---
#
#         # Обновляем игрока (движение по стрелкам)
#         player.update()
#
#         # Обновляем врага и монету
#         # (update() группы передаёт аргументы во все спрайты)
#         for e in enemies:
#             passed = e.update(speed)
#             if passed:
#                 score += 1
#         coins_group.update(speed)
#
#         # --- Collision: player vs enemy ---
#         if pygame.sprite.spritecollideany(player, enemies):
#             if crash_sound:
#                 crash_sound.play()
#
#             time.sleep(0.5)
#             screen.fill(RED)
#             screen.blit(game_over_text, (30, 250))
#             pygame.display.update()
#
#             # Очищаем спрайты
#             for entity in all_sprites:
#                 entity.kill()
#
#             time.sleep(2)
#             running = False
#             continue  # выходим из цикла, далее pygame.quit()
#
#         # --- Collision: player vs coin ---
#         hit_coin = pygame.sprite.spritecollideany(player, coins_group)
#         if hit_coin:
#             if coin_sound:
#                 coin_sound.play()
#             coins += 1
#             hit_coin.reset_position()
#
#         # --- Drawing ---
#         screen.blit(background, (0, 0))
#
#         # Текст: очки и монеты
#         score_surf = font_small.render(f"Score: {score}", True, BLACK)
#         coins_surf = font_small.render(f"Coins: {coins}", True, BLACK)
#
#         screen.blit(score_surf, (10, 10))
#         screen.blit(coins_surf, (SCREEN_WIDTH - 120, 10))
#
#         # Все спрайты
#         for entity in all_sprites:
#             screen.blit(entity.image, entity.rect)
#
#         pygame.display.update()
#         clock.tick(FPS)
#
#     pygame.quit()
#     sys.exit()
#
#
#
# main()


import sys
import time
import random
import pygame

# --- Initialization ---
pygame.init()

# --- Settings ---
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Начальная скорость, очки, монеты
START_SPEED = 5
SPEED_INCREASE_MS = 1000   # раз в 1 секунду увеличиваем скорость

# --- Colors ---
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- Asset paths ---
BG_IMAGE_PATH     = "AnimatedStreet.png"
PLAYER_IMAGE_PATH = "Player.png"
ENEMY_IMAGE_PATH  = "Enemy.png"
COIN_IMAGE_PATH   = "Coin.png"


# ============================
# --- Classes ---
# ============================

class Enemy(pygame.sprite.Sprite):
    """Вражеская машина, падает сверху вниз с заданной скоростью."""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ENEMY_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        """Выставляем врага наверх в случайную позицию по X."""
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self, speed: float):
        """Двигаем врага вниз с учётом текущей скорости."""
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()
            return True  # враг прошёл экран → +1 очко
        return False


class Player(pygame.sprite.Sprite):
    """Машина игрока, двигается влево-вправо по стрелкам."""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.speed_x = 5  # скорость по X

    def update(self):
        """Обрабатываем ввод и двигаем игрока."""
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed_x, 0)
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(self.speed_x, 0)


class Coin(pygame.sprite.Sprite):
    """Монета, падает сверху с меньшей скоростью, чем враг."""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(COIN_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        """Сбрасываем монету наверх в новую случайную позицию."""
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self, speed: float):
        """Двигаем монету вниз (чуть медленнее, чем враги)."""
        self.rect.move_ip(0, speed * 0.5)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()


# ============================
# --- Main Game ---
# ============================

def main():
    # --- Setup window, clock, fonts ---
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Racer (No Sounds)")

    clock = pygame.time.Clock()

    font_big = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over_text = font_big.render("Game Over", True, BLACK)

    # Фон
    background = pygame.image.load(BG_IMAGE_PATH).convert()

    # --- Game state ---
    score = 0
    coins = 0
    speed = START_SPEED

    # --- Sprites ---
    player = Player()
    enemy = Enemy()
    coin = Coin()

    enemies = pygame.sprite.Group(enemy)
    coins_group = pygame.sprite.Group(coin)
    all_sprites = pygame.sprite.Group(player, enemy, coin)

    # --- Custom event: speed increase ---
    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, SPEED_INCREASE_MS)

    running = True
    while running:
        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == INC_SPEED:
                speed += 0.5

        # --- Update logic ---
        player.update()

        for e in enemies:
            passed = e.update(speed)
            if passed:
                score += 1
        coins_group.update(speed)

        # --- Collision: player vs enemy ---
        if pygame.sprite.spritecollideany(player, enemies):
            time.sleep(0.5)
            screen.fill(RED)
            screen.blit(game_over_text, (30, 250))
            pygame.display.update()

            for entity in all_sprites:
                entity.kill()

            time.sleep(2)
            running = False
            continue

        # --- Collision: player vs coin ---
        hit_coin = pygame.sprite.spritecollideany(player, coins_group)
        if hit_coin:
            coins += 1
            hit_coin.reset_position()

        # --- Drawing ---
        screen.blit(background, (0, 0))

        score_surf = font_small.render(f"Score: {score}", True, BLACK)
        coins_surf = font_small.render(f"Coins: {coins}", True, BLACK)

        screen.blit(score_surf, (10, 10))
        screen.blit(coins_surf, (SCREEN_WIDTH - 120, 10))

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


main()
