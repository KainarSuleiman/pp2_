import sys
import random
import pygame

# -----------------------------
# Настройки игры
# -----------------------------
pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Стартовая скорость врага
START_SPEED = 5
# На сколько увеличиваем скорость при наборе порога монет
SPEED_STEP = 1.0
# Порог монет (по сумме веса), после которого увеличиваем скорость
COINS_FOR_SPEEDUP = 5

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Пути к ресурсам
BG_IMAGE_PATH     = "../pp2_labs_pg/AnimatedStreet.png"
PLAYER_IMAGE_PATH = "../pp2_labs_pg/Player.png"
ENEMY_IMAGE_PATH  = "../pp2_labs_pg/Enemy.png"
COIN_IMAGE_PATH   = "../pp2_labs_pg/Coin.png"
CRASH_SOUND_PATH  = "crash.wav"
COIN_SOUND_PATH   = "coin.wav"


# -----------------------------
# Классы спрайтов
# -----------------------------
class Enemy(pygame.sprite.Sprite):
    """Вражеская машина, двигается сверху вниз."""

    def _init_(self):
        super()._init_()
        self.image = pygame.image.load(ENEMY_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        """Ставим врага наверх в случайную позицию по X."""
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self, speed: float) -> None:
        """
        Двигаем врага вниз. Скорость передаётся параметром.
        Если он вышел за нижнюю границу, просто возвращаем наверх.
        """
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()


class Player(pygame.sprite.Sprite):
    """Машина игрока, управляется стрелками влево/вправо."""

    def _init_(self):
        super()._init_()
        self.image = pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect()
        # Стартовая позиция
        self.rect.center = (160, 520)
        self.speed_x = 5

    def update(self) -> None:
        """Обрабатываем нажатия клавиш и двигаем игрока."""
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed_x, 0)
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(self.speed_x, 0)


class Coin(pygame.sprite.Sprite):
    """
    Монета с весом (ценностью).
    Вес влияет на то, сколько монет добавляется в счётчик.
    """

    # Возможные веса монет
    WEIGHT_OPTIONS = [1, 2, 3]

    def _init_(self, font_small: pygame.font.Font):
        super()._init_()
        self.image_base = pygame.image.load(COIN_IMAGE_PATH).convert_alpha()
        self.rect = self.image_base.get_rect()
        self.font = font_small

        self.weight = 1
        self.image = self.image_base.copy()
        self.reset_position()

    def reset_position(self):
        """Ставим монету наверх в случайную позицию и выбираем новый вес."""
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.weight = random.choice(self.WEIGHT_OPTIONS)

        # Рисуем цифру веса поверх монеты
        self.image = self.image_base.copy()
        label = self.font.render(str(self.weight), True, BLACK)
        # Центрируем текст на монете
        label_rect = label.get_rect(center=self.rect.width // 2, centery=self.rect.height // 2)
        self.image.blit(label, label_rect)

    def update(self, speed: float) -> None:
        """Двигаем монету вниз (чуть медленнее врага)."""
        self.rect.move_ip(0, speed * 0.5)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()


# -----------------------------
# Основная функция игры
# -----------------------------
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Racer – Coins with Weights")

    clock = pygame.time.Clock()

    # Шрифты
    font_big = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over_text = font_big.render("Game Over", True, BLACK)

    # Фон
    background = pygame.image.load(BG_IMAGE_PATH).convert()

    # Счётчики
    score = 0          # очки за объезд врагов
    coins_value = 0    # сумма весов монет
    speed = START_SPEED
    next_speedup_at = COINS_FOR_SPEEDUP

    # Спрайты
    player = Player()
    enemy = Enemy()
    coin = Coin(font_small)

    enemies = pygame.sprite.Group(enemy)
    coins_group = pygame.sprite.Group(coin)
    all_sprites = pygame.sprite.Group(player, enemy, coin)

    # Звуки (делаем try/except, чтобы игра не падала, если файла нет)
    try:
        crash_sound = pygame.mixer.Sound(CRASH_SOUND_PATH)
    except pygame.error:
        crash_sound = None

    try:
        coin_sound = pygame.mixer.Sound(COIN_SOUND_PATH)
    except pygame.error:
        coin_sound = None

    running = True
    while running:
        # --- Обработка событий ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Логика игры ---

        # Обновляем игрока
        player.update()

        # Обновляем врага и монету
        enemies.update(speed)
        coins_group.update(speed)

        # Если враг вышел за экран вниз – плюс одно очко
        for e in enemies:
            if e.rect.top <= speed and e.rect.top > 0:
                # небольшой трюк: очки можно считать по событию, но можно и проще:
                pass
        # Правильнее считать так: если enemy пересёк нижнюю границу,
        # но мы уже сбросили позицию в update, поэтому проще:
        # будем инкрементировать score, когда enemy возвращаем наверх
        # Для этого можно доработать Enemy.update() и возвращать флаг.
        # Чтобы не усложнять, считаем по Y:
        if enemy.rect.top == 0 and enemy.rect.bottom <= speed + enemy.image.get_height():
            score += 1

        # Столкновение игрока с врагом
        if pygame.sprite.spritecollideany(player, enemies):
            if crash_sound:
                crash_sound.play()

            # Небольшая пауза и заставка Game Over
            pygame.time.delay(500)
            screen.fill(RED)
            screen.blit(game_over_text, (30, 250))
            pygame.display.update()

            pygame.time.delay(2000)
            running = False
            continue

        # Столкновение игрока с монетой
        hit_coin = pygame.sprite.spritecollideany(player, coins_group)
        if hit_coin:
            if coin_sound:
                coin_sound.play()

            # Добавляем к общему значению монет вес пойманной
            coins_value += hit_coin.weight
            # Проверяем, нужно ли ускорить врага
            if coins_value >= next_speedup_at:
                speed += SPEED_STEP
                next_speedup_at += COINS_FOR_SPEEDUP
            # Перемещаем монету наверх в новую позицию и с новым весом
            hit_coin.reset_position()

        # --- Отрисовка ---
        screen.blit(background, (0, 0))

        # Текст: Score и Coins
        score_surf = font_small.render(f"Score: {score}", True, BLACK)
        coins_surf = font_small.render(f"Coins: {coins_value}", True, BLACK)
        screen.blit(score_surf, (10, 10))
        screen.blit(coins_surf, (SCREEN_WIDTH - 140, 10))

        # Отрисовываем все спрайты
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()



main()
