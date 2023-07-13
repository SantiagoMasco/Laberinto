import pygame

global_x = 1
global_y = 0

def draw_maze(maze, screen, screen_width, screen_height):
    block_size = 25

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (col * block_size, row * block_size, block_size, block_size))
            elif maze[row][col] == 2:
                pygame.draw.rect(screen, (0, 0, 255), (col * block_size, row * block_size, block_size, block_size))
            elif maze[row][col] == 3:
                pygame.draw.rect(screen, (0, 255, 0), (col * block_size, row * block_size, block_size, block_size))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (col * block_size, row * block_size, block_size, block_size))

    pygame.display.flip()


def start_game():
    global global_x, global_y

    screen_width = 800
    screen_height = 600

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("maze")

    with open("maze.txt", "r") as file:
        maze = [[int(cell) for cell in line.strip().split(",")] for line in file if line.strip()]

    running = True
    while running:
        maze[global_y][global_x] = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if global_y > 0:
                        if maze[global_y - 1][global_x] != 0:
                            maze[global_y][global_x] = 1
                            global_y -= 1
                            maze[global_y][global_x] = 2
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if global_y < len(maze) - 1:
                        if maze[global_y + 1][global_x] != 0:
                            maze[global_y][global_x] = 1
                            global_y += 1
                            maze[global_y][global_x] = 2
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if global_x < len(maze[0]) - 1:
                        if maze[global_y][global_x + 1] != 0:
                            maze[global_y][global_x] = 1
                            global_x += 1
                            maze[global_y][global_x] = 2
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if global_x > 0:
                        if maze[global_y][global_x - 1] != 0:
                            maze[global_y][global_x] = 1
                            global_x -= 1
                            maze[global_y][global_x] = 2
        draw_maze(maze, screen, screen_width, screen_height)
        if maze[19][28] == 2:
            running = False

    pygame.quit()


start_game()
