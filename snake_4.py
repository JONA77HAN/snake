import pygame
import random

pygame.init()

# Configuración de la pantalla
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Tamaño de la serpiente y de la comida
block_size = 20

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

# Cargar los fondos
backgrounds = [
    pygame.image.load("fondos/fondo_nivel_1.jpg"),
    pygame.image.load("fondos/fondo_nivel_2.jpg"),
    pygame.image.load("fondos/fondo_nivel_3.jpeg"),
    pygame.image.load("fondos/fondo_nivel_4.jpg"),
    pygame.image.load("fondos/fondo_nivel_5.jpeg")
]

current_background = 0  # Índice del fondo actual

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, green, [segment[0], segment[1], block_size, block_size])

def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width / 2 - mesg.get_width() / 2, height / 2 - mesg.get_height() / 2])

def game_loop():
    global apple_count, current_background
    game_over = False
    game_close = False

    snake_list = []
    length_of_snake = 1

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("¡Perdiste! Presiona Q para salir o C para jugar de nuevo.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.blit(backgrounds[current_background], (0, 0))  # Dibujar el fondo actual

        pygame.draw.rect(screen, white, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)

        apple_counter_text = font.render("Manzanas: " + str(apple_count), True, white)
        screen.blit(apple_counter_text, (10, 10))

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            length_of_snake += 1
            apple_count += 1

            if apple_count >= 10:
                current_background = (current_background + 1) % len(backgrounds)

        clock.tick(15)

    pygame.quit()
    quit()

apple_count = 0
game_loop()
