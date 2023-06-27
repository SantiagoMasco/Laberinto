import pygame


def draw_maze(maze, screen, screen_width, screen_height):
    block_size = 25



    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (col * block_size, row * block_size, block_size, block_size))
            elif maze[row][col] == 2:
                pygame.draw.rect(screen, (0, 0, 255), (col * block_size, row * block_size, block_size, block_size))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (col * block_size, row * block_size, block_size, block_size))

    pygame.display.flip()


def start_game():
    screen_width = 800
    screen_height = 600

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("maze")

    with open("maze.txt", "r") as file:
        maze = [[int(cell) for cell in line.strip().split(",")] for line in file if line.strip()]
        x = 1
        y = 0

    running = True
    while running:
        maze[y][x] = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if(y > 0):
                        if(maze[y-1][x] != 0):
                            maze[y][x] = 1
                            y -= 1
                            maze[y][x] = 2
                if event.key == pygame.K_s:
                    if(maze[y+1][x] != 0):
                        maze[y][x] = 1
                        y += 1
                        maze[y][x] = 2
                if event.key == pygame.K_d:
                    if (maze[y][x + 1] != 0):
                        maze[y][x] = 1
                        x += 1
                        maze[y][x] = 2
                if event.key == pygame.K_a:
                    if (maze[y][x - 1] != 0):
                        maze[y][x] = 1
                        x -= 1
                        maze[y][x] = 2
        draw_maze(maze, screen, screen_width, screen_height)
        if(maze[19][28] == 2):
            running = False

    pygame.quit()


start_game()
