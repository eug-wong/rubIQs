import pygame
from pygame.locals import *
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Set up the window dimensions
WIDTH = 800
HEIGHT = 800
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption("Rubik's Cube in Pygame")

# Define cube colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Define cube size and positions
cube_size = 100

projection_matrix = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]

cube_points = [n for n in range(8)]
cube_points[0] = [-1, -1, 1]
cube_points[1] = [1, -1, 1]
cube_points[2] = [1, 1, 1]
cube_points[3] = [-1, 1, 1]
cube_points[4] = [-1, -1, -1]
cube_points[5] = [1, -1, -1]
cube_points[6] = [1, 1, -1]
cube_points[7] = [-1, 1, -1]


def connect_points(i, j, points):
    pygame.draw.line(window, (0,0,0), (points[i][0], points[i][1]), (points[j][0], points[j][1]))

# Main game loop
running = True
x = y = z = 0

while running:
    clock.tick(60)
    window.fill(WHITE)
    
    rotation_x = [[1, 0, 0],
                  [0, math.cos(x), -math.sin(x)],
                  [0, math.sin(x), math.cos(x)]]
    
    rotation_y = [[math.cos(y), 0, math.sin(y)],
                  [0, 1, 0],
                  [-math.sin(y), 0, math.cos(y)]]
    
    rotation_z = [[math.cos(z), -math.sin(z), 0],
                  [math.sin(z), math.cos(z), 0],
                  [0, 0, 1]]

    points = [0 for _ in range(len(cube_points))]
    i = 0


    for point in cube_points:
        rotate_x = np.dot(rotation_x, point)
        rotate_y = np.dot(rotation_y, rotate_x)
        rotate_z = np.dot(rotation_z, rotate_y)
        point_2d = np.dot(projection_matrix, rotate_z)
        point_x = (point_2d[0] * cube_size) + WIDTH / 2
        point_y = (point_2d[1] * cube_size) + HEIGHT / 2
        

        points[i] = (point_x, point_y)
        i += 1

        x += 0.0001
        y += 0.001

    
    connect_points(0, 1, points)
    connect_points(1, 2, points)
    connect_points(2, 3, points)
    connect_points(3, 0, points)
    connect_points(4, 5, points)
    connect_points(5, 6, points)
    connect_points(6, 7, points)
    connect_points(7, 4, points)
    connect_points(0, 4, points)
    connect_points(1, 5, points)
    connect_points(2, 6, points)
    connect_points(3, 7, points)



    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()

# Quit Pygame
pygame.quit()