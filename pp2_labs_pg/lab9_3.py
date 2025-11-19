import pygame
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)

# Цвет кисти по умолчанию
DRAW_COLOR = (0, 0, 0)

# Толщина линий
LINE_WIDTH = 3


def draw_shape(surface, tool, start_pos, end_pos, color, width):
    """
    Рисует выбранную фигуру на surface.
    tool:
      'line', 'rect', 'square',
      'right_tri', 'eq_tri', 'rhombus'
    """
    x1, y1 = start_pos
    x2, y2 = end_pos

    left = min(x1, x2)
    right = max(x1, x2)
    top = min(y1, y2)
    bottom = max(y1, y2)
    w = right - left
    h = bottom - top

    if tool == "line":
        pygame.draw.line(surface, color, start_pos, end_pos, width)

    elif tool == "rect":
        rect = pygame.Rect(left, top, w, h)
        pygame.draw.rect(surface, color, rect, width)

    elif tool == "square":
        # Строим квадрат по минимальной стороне
        side = min(w, h)
        rect = pygame.Rect(left, top, side, side)
        pygame.draw.rect(surface, color, rect, width)

    elif tool == "right_tri":
        # Прямоугольный треугольник:
        # прямой угол в левом нижнем углу bounding-box
        p1 = (left, bottom)   # прямой угол
        p2 = (left, top)
        p3 = (right, bottom)
        pygame.draw.polygon(surface, color, [p1, p2, p3], width)

    elif tool == "eq_tri":
        # Равносторонний треугольник:
        # основание горизонтально, вершина сверху.
        # Берём сторону как ширину bounding-box.
        side = w
        if side == 0:
            return
        height = int(side * math.sqrt(3) / 2)

        # Вершина
        apex_x = left + side // 2
        apex_y = top
        # Основание
        p2 = (left, top + height)
        p3 = (left + side, top + height)
        pygame.draw.polygon(surface, color, [(apex_x, apex_y), p2, p3], width)

    elif tool == "rhombus":
        # Ромб: вершины в серединах сторон bounding-box
        cx = (left + right) // 2
        cy = (top + bottom) // 2
        top_pt = (cx, top)
        right_pt = (right, cy)
        bottom_pt = (cx, bottom)
        left_pt = (left, cy)
        pygame.draw.polygon(surface, color, [top_pt, right_pt, bottom_pt, left_pt], width)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Paint – Squares, Triangles, Rhombus")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    # Отдельная поверхность-холст, чтобы рисунок не стирался при обновлении
    canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    canvas.fill(BG_COLOR)

    # Текущее состояние инструмента
    tool = "line"
    drawing = False
    start_pos = (0, 0)
    current_pos = (0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            # Выход из программы
            if event.type == pygame.QUIT:
                running = False

            # Смена инструмента клавишами
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    tool = "line"
                elif event.key == pygame.K_2:
                    tool = "rect"
                elif event.key == pygame.K_3:
                    tool = "square"
                elif event.key == pygame.K_4:
                    tool = "right_tri"
                elif event.key == pygame.K_5:
                    tool = "eq_tri"
                elif event.key == pygame.K_6:
                    tool = "rhombus"
                elif event.key == pygame.K_c:
                    # Очистка холста по C
                    canvas.fill(BG_COLOR)

            # Начало рисования
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True
                start_pos = event.pos
                current_pos = event.pos

            # Обновляем текущую позицию при движении мыши
            if event.type == pygame.MOUSEMOTION and drawing:
                current_pos = event.pos

            # Завершение рисования – окончательно рисуем фигуру на canvas
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and drawing:
                drawing = False
                end_pos = event.pos
                draw_shape(canvas, tool, start_pos, end_pos, DRAW_COLOR, LINE_WIDTH)

        # Отрисовка кадра
        screen.fill(BG_COLOR)
        # Сначала рисуем постоянный холст
        screen.blit(canvas, (0, 0))

        # Если сейчас рисуем – отображаем временный "превью" на экране
        if drawing:
            draw_shape(screen, tool, start_pos, current_pos, DRAW_COLOR, LINE_WIDTH)

        # Подпись с подсказками
        help_text = (
            "1-Line  2-Rect  3-Square  4-Right Tri  "
            "5-Equilateral Tri  6-Rhombus  C-Clear"
        )
        label = font.render(help_text, True, (0, 0, 0))
        screen.blit(label, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



    main()