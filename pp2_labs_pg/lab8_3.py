
import pygame

BG_COLOR = (255, 255, 255)   # цвет фона (белый)
SCREEN_SIZE = (640, 480)


def draw_text(screen, text, pos, font, color=(0, 0, 0)):
    """Простой вывод текста."""
    img = font.render(text, True, color)
    screen.blit(img, pos)


def make_palette():
    """Создаём список (color, rect) для палитры."""
    colors = [
        (0, 0, 0),       # чёрный
        (255, 0, 0),     # красный
        (0, 255, 0),     # зелёный
        (0, 0, 255),     # синий
        (255, 255, 0),   # жёлтый
        (255, 0, 255),   # маджента
        (0, 255, 255),   # циан
    ]
    palette_rects = []
    x0 = 10
    y0 = 10
    size = 30
    margin = 5

    for i, c in enumerate(colors):
        rect = pygame.Rect(x0 + i * (size + margin), y0, size, size)
        palette_rects.append((c, rect))
    return palette_rects


def draw_palette(screen, palette_rects, current_color):
    """Рисуем палитру и рамку вокруг выбранного цвета."""
    for color, rect in palette_rects:
        pygame.draw.rect(screen, color, rect)
        if color == current_color:
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)


def get_palette_color_at(palette_rects, pos):
    """Если кликнули по палитре — вернуть цвет, иначе None."""
    for color, rect in palette_rects:
        if rect.collidepoint(pos):
            return color
    return None


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("PyGame Input Example – Extended Paint")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Arial", 18)

    # --- переменные как в примере + новые ---

    radius = 15
    mode = 'blue'          # цветовой режим, как в примере (r/g/b)
    tool = 'brush'         # 'brush', 'rect', 'circle', 'eraser'

    # текущий цвет (по умолчанию синий)
    current_color = (0, 0, 255)

    # поверхность, на которой мы рисуем (холст)
    drawing = pygame.Surface(SCREEN_SIZE)
    drawing.fill(BG_COLOR)

    # для кисти / ластика
    last_pos = None

    # для прямоугольника/круга (рисование по зажатию)
    drawing_shape = False
    shape_start = (0, 0)
    shape_end = (0, 0)

    # палитра
    palette_rects = make_palette()

    while True:
        # --- как в оригинальном примере: polling клавиатуры ---
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        # --- обработка событий ---
        for event in pygame.event.get():
            # выход
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                # те же сочетания, что в примере
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # выбор инструмента
                if event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rect'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'

                # выбор цвета клавишами (как в оригинале)
                if event.key == pygame.K_r:
                    mode = 'red'
                    current_color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    mode = 'green'
                    current_color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    mode = 'blue'
                    current_color = (0, 0, 255)

            # мышь
            if event.type == pygame.MOUSEBUTTONDOWN:
                # изменение радиуса колёсиком (4/5 — wheel up/down)
                if event.button == 4:     # wheel up
                    radius = min(100, radius + 1)
                elif event.button == 5:   # wheel down
                    radius = max(1, radius - 1)

                if event.button == 1:     # левая кнопка
                    # сначала проверяем палитру
                    palette_color = get_palette_color_at(palette_rects, event.pos)
                    if palette_color is not None:
                        current_color = palette_color
                        # доп. режим, но логически нам уже не важен mode ('red/green/blue')
                    else:
                        # не попали в палитру — начинаем рисовать
                        if tool in ('brush', 'eraser'):
                            last_pos = event.pos
                            color = BG_COLOR if tool == 'eraser' else current_color
                            pygame.draw.circle(drawing, color, event.pos, radius)
                        elif tool in ('rect', 'circle'):
                            drawing_shape = True
                            shape_start = event.pos
                            shape_end = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    # заканчиваем фигуру
                    if drawing_shape and tool in ('rect', 'circle'):
                        shape_end = event.pos
                        x1, y1 = shape_start
                        x2, y2 = shape_end
                        left = min(x1, x2)
                        top = min(y1, y2)
                        width = abs(x2 - x1)
                        height = abs(y2 - y1)

                        if width > 0 and height > 0:
                            if tool == 'rect':
                                rect = pygame.Rect(left, top, width, height)
                                pygame.draw.rect(drawing, current_color, rect, 2)
                            elif tool == 'circle':
                                # окружность по меньшей стороне
                                radius_c = int(min(width, height) / 2)
                                center = (left + width // 2, top + height // 2)
                                pygame.draw.circle(drawing, current_color, center, radius_c, 2)

                    drawing_shape = False
                    shape_start = shape_end
                    last_pos = None

            if event.type == pygame.MOUSEMOTION:
                # если зажата левая кнопка и выбран инструмент кисти / ластика
                if event.buttons[0] and tool in ('brush', 'eraser'):
                    if last_pos is None:
                        last_pos = event.pos
                    color = BG_COLOR if tool == 'eraser' else current_color
                    pygame.draw.line(drawing, color, last_pos, event.pos, radius * 2)
                    last_pos = event.pos

                # если рисуем фигуру — просто обновляем конечную точку для предпросмотра
                if event.buttons[0] and drawing_shape and tool in ('rect', 'circle'):
                    shape_end = event.pos

        # --- отрисовка кадра ---
        screen.fill(BG_COLOR)

        # 1) рисуем постоянный холст
        screen.blit(drawing, (0, 0))

        # 2) если сейчас тянем прямоугольник/круг — рисуем предпросмотр
        if drawing_shape and tool in ('rect', 'circle'):
            x1, y1 = shape_start
            x2, y2 = shape_end
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)

            if width > 0 and height > 0:
                if tool == 'rect':
                    rect = pygame.Rect(left, top, width, height)
                    pygame.draw.rect(screen, current_color, rect, 1)
                elif tool == 'circle':
                    radius_c = int(min(width, height) / 2)
                    center = (left + width // 2, top + height // 2)
                    pygame.draw.circle(screen, current_color, center, radius_c, 1)

        # 3) палитра + подписи
        draw_palette(screen, palette_rects, current_color)

        draw_text(
            screen,
            f"Tool: {tool} (1-Brush, 2-Rect, 3-Circle, 4-Eraser)",
            (10, 50),
            font
        )
        draw_text(
            screen,
            f"Color: {current_color} (click palette / R,G,B)",
            (10, 70),
            font
        )
        draw_text(
            screen,
            f"Radius: {radius} (mouse wheel)",
            (10, 90),
            font
        )

        pygame.display.flip()
        clock.tick(60)



main()

