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
                    move_up(maze)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_down(maze)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_right(maze)
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_left(maze)
        draw_maze(maze, screen, screen_width, screen_height)
        if maze[19][28] == 2:
            running = False

    pygame.quit()


def move_up(maze):
    global global_x, global_y
    if global_y > 0 and maze[global_y - 1][global_x] != 0:
        maze[global_y][global_x] = 1
        global_y -= 1
        maze[global_y][global_x] = 2
    return maze


def move_down(maze):
    global global_x, global_y
    if global_y < len(maze) - 1 and maze[global_y + 1][global_x] != 0:
        maze[global_y][global_x] = 1
        global_y += 1
        maze[global_y][global_x] = 2
    return maze


def move_right(maze):
    global global_x, global_y
    if global_x < len(maze[0]) - 1 and maze[global_y][global_x + 1] != 0:
        maze[global_y][global_x] = 1
        global_x += 1
        maze[global_y][global_x] = 2
    return maze


def move_left(maze):
    global global_x, global_y
    if global_x > 0 and maze[global_y][global_x - 1] != 0:
        maze[global_y][global_x] = 1
        global_x -= 1
        maze[global_y][global_x] = 2
    return maze


start_game()

"""


import pygame
import random

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

        # Generar número aleatorio del 1 al 4
        random_move = random.randint(1, 4)

        if random_move == 1:
            move_down(maze)
        elif random_move == 2:
            move_up(maze)
        elif random_move == 3:
            move_right(maze)
        elif random_move == 4:
            move_left(maze)

        draw_maze(maze, screen, screen_width, screen_height)
        if maze[19][28] == 2:
            running = False

    pygame.quit()


def move_up(maze):
    global global_x, global_y
    if global_y > 0 and maze[global_y - 1][global_x] != 0:
        maze[global_y][global_x] = 1
        global_y -= 1
        maze[global_y][global_x] = 2
    return maze


def move_down(maze):
    global global_x, global_y
    if global_y < len(maze) - 1 and maze[global_y + 1][global_x] != 0:
        maze[global_y][global_x] = 1
        global_y += 1
        maze[global_y][global_x] = 2
    return maze


def move_right(maze):
    global global_x, global_y
    if global_x < len(maze[0]) - 1 and maze[global_y][global_x + 1] != 0:
        maze[global_y][global_x] = 1
        global_x += 1
        maze[global_y][global_x] = 2
    return maze


def move_left(maze):
    global global_x, global_y
    if global_x > 0 and maze[global_y][global_x - 1] != 0:
        maze[global_y][global_x] = 1
        global_x -= 1
        maze[global_y][global_x] = 2
    return maze


start_game()

"""