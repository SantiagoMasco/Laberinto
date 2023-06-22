import pygame


def draw_maze(maze, screen, screen_width, screen_height):
    block_size = 25



    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (col * block_size, row * block_size, block_size, block_size))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (col * block_size, row * block_size, block_size, block_size))

    pygame.display.flip()


def start_game():
    screen_width = 800
    screen_height = 600

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Laberinto")

    with open("laberinto.txt", "r") as file:
        laberinto = [[int(cell) for cell in line.strip().split(",")] for line in file if line.strip()]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_maze(laberinto, screen, screen_width, screen_height)  # Dibujar el laberinto en la ventana

    pygame.quit()


start_game()
