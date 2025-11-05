import pygame, sys, random, time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

CELL_SIZE = 20
WIDTH = 600
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Verdana", 20)

snake_pos = [[100, 50], [80, 50], [60, 50]]
direction = "RIGHT"
change_to = direction
food_pos = [random.randrange(1, WIDTH//CELL_SIZE) * CELL_SIZE,
            random.randrange(1, HEIGHT//CELL_SIZE) * CELL_SIZE]
food_spawn = True
score = 0
level = 1
speed = 10

clock = pygame.time.Clock()

def show_info():
    score_text = font.render(f"Score: {score}", True, BLUE)
    level_text = font.render(f"Level: {level}", True, BLUE)
    SCREEN.blit(score_text, (10, 10))
    SCREEN.blit(level_text, (WIDTH - 120, 10))

def game_over():
    game_over_text = font.render("Game Over! Press any key to exit.", True, RED)
    SCREEN.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    direction = change_to

    if direction == "UP":
        snake_pos[0][1] -= CELL_SIZE
    if direction == "DOWN":
        snake_pos[0][1] += CELL_SIZE
    if direction == "LEFT":
        snake_pos[0][0] -= CELL_SIZE
    if direction == "RIGHT":
        snake_pos[0][0] += CELL_SIZE

    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or
        snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT):
        game_over()

    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over()

    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = False
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake_pos.pop()

    if not food_spawn:
        while True:
            x = random.randrange(1, WIDTH//CELL_SIZE) * CELL_SIZE
            y = random.randrange(1, HEIGHT//CELL_SIZE) * CELL_SIZE
            if [x, y] not in snake_pos:
                food_pos = [x, y]
                break
        food_spawn = True

    snake_pos.insert(0, list(snake_pos[0]))

    SCREEN.fill(WHITE)
    for pos in snake_pos:
        pygame.draw.rect(SCREEN, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(SCREEN, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    show_info()
    pygame.display.update()
    clock.tick(speed)
