import pygame
import random
import sys

# -----------------------------
# Настройки игры
# -----------------------------
pygame.init()

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

FPS = 10

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE  = (0, 0, 255)

# Описание типов еды: цвет + вес (очки)
FOOD_TYPES = [
    {"color": (0, 255, 0),   "weight": 1},  # зелёная – 1 очко
    {"color": (255, 165, 0), "weight": 3},  # оранжевая – 3 очка
    {"color": (255, 0, 0),   "weight": 5},  # красная – 5 очков
]

FOOD_LIFETIME_MS = 7000  # еда живёт 7 секунд


# -----------------------------
# Вспомогательные функции
# -----------------------------
def get_random_free_cell(snake):
    """Находим случайную клетку, в которой нет змейки."""
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if (x, y) not in snake:
            return (x, y)


def spawn_food(snake):
    """
    Создаём "объект еды" как словарь:
    {
      "pos": (x, y),
      "color": (r,g,b),
      "weight": int,
      "spawn_time": int (миллисекунды)
    }
    """
    cell = get_random_free_cell(snake)
    food_type = random.choice(FOOD_TYPES)
    return {
        "pos": cell,
        "color": food_type["color"],
        "weight": food_type["weight"],
        "spawn_time": pygame.time.get_ticks()
    }


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake – Food Weights & Timer")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    # Состояние змейки: список клеток, первая – голова
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = (1, 0)  # движемся вправо

    score = 0

    # Создаём первую еду
    food = spawn_food(snake)

    running = True
    while running:
        # --- Обработка событий ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Управление направлением (запрещён поворот на 180 градусов)
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # --- Движение змейки ---
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Проверка выхода за границы
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            break  # Game Over

        # Проверка столкновения с собой
        if new_head in snake:
            break  # Game Over

        # Добавляем голову
        snake.insert(0, new_head)

        # --- Проверка еды ---
        if new_head == food["pos"]:
            # Добавляем очки по весу еды
            score += food["weight"]
            # Генерируем новую еду
            food = spawn_food(snake)
        else:
            # Если не съели – убираем хвост (движение без роста)
            snake.pop()

        # --- Проверка таймера еды ---
        now = pygame.time.get_ticks()
        if now - food["spawn_time"] > FOOD_LIFETIME_MS:
            # Текущая еда "пропала" – создаём новую
            food = spawn_food(snake)

        # --- Отрисовка ---
        screen.fill(BLACK)

        # Еда
        fx, fy = food["pos"]
        pygame.draw.rect(
            screen,
            food["color"],
            (fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

        # Змейка
        for i, (sx, sy) in enumerate(snake):
            color = BLUE if i == 0 else GREEN  # голова синяя, тело зелёное
            pygame.draw.rect(
                screen,
                color,
                (sx * CELL_SIZE, sy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

        # Текст со счётом и весом текущей еды
        score_text = font.render(f"Score: {score}", True, WHITE)
        weight_text = font.render(f"Food weight: {food['weight']}", True, WHITE)
        screen.blit(score_text, (10, 5))
        screen.blit(weight_text, (10, 25))

        pygame.display.flip()
        clock.tick(FPS)

    # Конец игры
    pygame.quit()
    sys.exit()



main()