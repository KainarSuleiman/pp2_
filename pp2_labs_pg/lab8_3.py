import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)
ERASER_COLOR = WHITE

screen.fill(WHITE)

drawing = False
last_pos = None
mode = "line"
color = BLACK
radius = 5

font = pygame.font.SysFont("Verdana", 18)

def draw_menu():
    text = font.render(f"Mode: {mode} | Color: {color}", True, BLACK)
    screen.blit(text, (10, 10))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos
        elif event.type == MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if mode == "rect":
                pygame.draw.rect(screen, color, pygame.Rect(
                    min(start_pos[0], end_pos[0]),
                    min(start_pos[1], end_pos[1]),
                    abs(end_pos[0]-start_pos[0]),
                    abs(end_pos[1]-start_pos[1])
                ), 2)
            elif mode == "circle":
                radius_circle = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, radius_circle, 2)
        elif event.type == MOUSEMOTION and drawing:
            if mode == "line":
                pygame.draw.line(screen, color, last_pos, event.pos, radius)
                last_pos = event.pos
            elif mode == "eraser":
                pygame.draw.line(screen, ERASER_COLOR, last_pos, event.pos, radius * 2)
                last_pos = event.pos
        elif event.type == KEYDOWN:
            if event.key == K_r:
                mode = "rect"
            elif event.key == K_c:
                mode = "circle"
            elif event.key == K_l:
                mode = "line"
            elif event.key == K_e:
                mode = "eraser"
            elif event.key == K_1:
                color = BLACK
            elif event.key == K_2:
                color = RED
            elif event.key == K_3:
                color = GREEN
            elif event.key == K_4:
                color = BLUE
            elif event.key == K_5:
                color = YELLOW
            elif event.key == K_s:
                pygame.image.save(screen, "drawing.png")

    info_surface = pygame.Surface((WIDTH, 30))
    info_surface.fill(WHITE)
    screen.blit(info_surface, (0, 0))
    draw_menu()
    pygame.display.update()
