
import pygame
import random
import sys

# --- Константы настройки игры ---

# Размер одной клетки (в пикселях)
CELL_SIZE = 20

# Размер игрового поля в клетках
GRID_WIDTH = 30   # 30 клеток по горизонтали
GRID_HEIGHT = 20  # 20 клеток по вертикали

# Размер окна
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE

# Цвета (R, G, B)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 200, 0)
COLOR_RED = (200, 0, 0)
COLOR_BLUE = (0, 0, 200)
COLOR_GRAY = (80, 80, 80)

# Настройки уровней
FOODS_PER_LEVEL = 3          # сколько фруктов нужно съесть для перехода на следующий уровень
INITIAL_SPEED = 8            # начальная скорость (кадров в секунду)
SPEED_INCREMENT_PER_LEVEL = 2   # насколько увеличивается скорость при новом уровне

# --- Вспомогательные функции ---

def draw_text(surface, text, x, y, font, color=COLOR_WHITE):
    """Рисует текст на заданной поверхности."""
    render = font.render(text, True, color)
    surface.blit(render, (x, y))


def get_random_free_cell(snake, walls):
    """
    Возвращает случайную свободную клетку (x, y),
    которая НЕ занята змеёй и стенами.
    """
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        pos = (x, y)
        if pos not in snake and pos not in walls:
            return pos


def create_walls():
    """
    Создаём набор стен (препятствий) внутрь поля.
    Можно настроить по своему (добавить/убрать блоки).
    """
    walls = []

    # Пример: вертикальная стенка посередине
    for y in range(5, 15):
        walls.append((15, y))

    # Пример: небольшая горизонтальная стенка
    for x in range(5, 10):
        walls.append((x, 3))

    return walls

# --- Основная функция игры ---

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake with Levels")
    clock = pygame.time.Clock()

    # Шрифт для вывода счёта и уровня
    font = pygame.font.SysFont("Arial", 20)

    # --- Инициализация состояния игры ---

    # Змейка: список координат (x, y) в клетках. Первый элемент — голова.
    snake = [(5, 5), (4, 5), (3, 5)]  # стартуем из трёх сегментов

    # Текущее направление движения змейки (dx, dy).
    # dx = 1, dy = 0 → движемся вправо
    direction = (1, 0)

    # Стены на поле
    walls = create_walls()

    # Счёт и уровни
    score = 0          # очки
    level = 1          # уровень
    foods_eaten = 0    # сколько фруктов съедено на текущем уровне

    # Скорость в кадрах в секунду
    speed = INITIAL_SPEED

    # Генерируем первую еду
    food = get_random_free_cell(snake, walls)

    running = True
    while running:
        # --- Обработка событий (клавиатура, выход) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Управление стрелками
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    # Не даём развернуться на 180 градусов
                    if direction != (0, 1):
                        direction = (0, -1)
                elif event.key == pygame.K_s:
                    if direction != (0, -1):
                        direction = (0, 1)
                elif event.key == pygame.K_a:
                    if direction != (1, 0):
                        direction = (-1, 0)
                elif event.key == pygame.K_d:
                    if direction != (-1, 0):
                        direction = (1, 0)
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # --- Логика двиdжения змейки ---

        # Текущая позиция головы
        head_x, head_y = snake[0]
        dx, dy = direction

        # Новая позиция головы
        new_head = (head_x + dx, head_y + dy)

        # 1) Проверка выхода за границы (столкновение со стеной поля)
        #    Если координата выходит за пределы [0, GRID_WIDTH-1] / [0, GRID_HEIGHT-1] → game over
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            print("Game over: вы вышли за границы поля")
            running = False

        # 2) Проверка столкновения с самим собой
        if new_head in snake:
            print("Game over: вы врезались в себя")
            running = False

        # 3) Проверка столкновения со стенами-препятствиями
        if new_head in walls:
            print("Game over: вы врезались в стену")
            running = False

        if not running:
            break

        # Добавляем новую голову в начало списка
        snake.insert(0, new_head)

        # --- Проверка на поедание еды ---
        if new_head == food:
            # Змейка съела еду: увеличиваем счёт, не удаляем хвост (змейка растёт)
            score += 10        # например, по 10 очков за еду
            foods_eaten += 1   # увеличиваем счётчик съеденных фруктов для уровня

            # Генерируем новый фрукт в свободной клетке
            food = get_random_free_cell(snake, walls)

            # --- Проверка на переход уровня ---
            if foods_eaten >= FOODS_PER_LEVEL:
                level += 1
                foods_eaten = 0
                # Увеличиваем скорость на новом уровне
                speed += SPEED_INCREMENT_PER_LEVEL
                print(f"Level up! Новый уровень: {level}, скорость: {speed}")
        else:
            # Если еду не съели — удаляем последний сегмент (хвост)
            snake.pop()

        # --- Отрисовка ---

        screen.fill(COLOR_BLACK)

        # Рисуем стены
        for (wx, wy) in walls:
            pygame.draw.rect(
                screen,
                COLOR_GRAY,
                (wx * CELL_SIZE, wy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

        # Рисуем еду
        pygame.draw.rect(
            screen,
            COLOR_RED,
            (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

        # Рисуем змейку
        for i, (sx, sy) in enumerate(snake):
            # Голова другим цветом (например, синим)
            color = COLOR_BLUE if i == 0 else COLOR_GREEN
            pygame.draw.rect(
                screen,
                color,
                (sx * CELL_SIZE, sy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

        # Рисуем счёт и уровень
        draw_text(screen, f"Score: {score}", 10, 5, font)
        draw_text(screen, f"Level: {level}", 10, 25, font)

        pygame.display.flip()

        # Ограничиваем FPS согласно текущей скорости (чем выше speed, тем быстрее игра)
        clock.tick(speed)

    # Завершение Pygame
    pygame.quit()
    sys.exit()

main()

