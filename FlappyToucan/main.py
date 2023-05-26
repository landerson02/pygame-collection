import pygame
from pygame.locals import *
import random
import Toucan
import Files
import Obstacle

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 650
GAP = 150
score = 0
main_menu = True
run = False
end_screen = False
frame = 0
a = 0
bgx = 0


def text(t, c, size):
    font = pygame.font.SysFont("arial", size)
    t = font.render(t, True, c)
    return t


pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Toucan")
clock = pygame.time.Clock()

toucan = Toucan.Toucan(100, 300, 0, False)
obstacles = [Obstacle.Obstacle(1000, random.randint(100, 550)), Obstacle.Obstacle(1500, random.randint(100, 550))]


def reset():
    obstacles[0].x = 1000
    obstacles[1].x = 1500
    toucan.y = 300


while main_menu:
    frame += 1
    if frame % 10 == 0:
        bgx -= 1
    clock.tick(60)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            main_menu = False
        if event.type == KEYDOWN and event.key == K_SPACE:
            score = 0
            run = True

    for i in range(10):
        win.blit(Files.bg_file, (bgx + 1000 * i, 0))
    win.blit(text("Flappy Toucan", (0, 0, 0), 70), (25, 30))
    win.blit(text("Space to Play!", (255, 255, 255), 50), (100, 450))
    win.blit(Files.toucan_file[a], (toucan.x, toucan.y))
    if frame % 30 == 0:
        if a == 1:
            a = 0
        else:
            a = 1
    if score > 0:
        win.blit(text("Score: %s" % score, (255, 255, 255), 60), (150, 200))

    while run:
        clock.tick(60)
        pygame.display.update()
        frame += 1
        if frame % 10 == 0:
            bgx -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu, run = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                main_menu, run = False
            if event.type == KEYDOWN and event.key == K_SPACE:
                toucan.fly_up()
        for i in range(10):
            win.blit(Files.bg_file, (bgx + 1000 * i, 0))
        if toucan.vel < 0:
            win.blit(Files.toucan_file[1], (toucan.x, toucan.y))
        else:
            win.blit(Files.toucan_file[0], (toucan.x, toucan.y))
        toucan.gravity()
        if toucan.y >= 610:
            toucan.y = 610

        for obstacle in obstacles:
            if obstacle.x < -80:
                obstacle.x += 1000
                obstacle.new_y()
            if obstacle.x - 80 == toucan.x:
                score += 1

            win.blit(Files.obstacle_files[0], (obstacle.x, obstacle.y - 550))
            win.blit(Files.obstacle_files[1], (obstacle.x, obstacle.y + GAP))
            obstacle.move()
            win.blit(text("Score: %s" % score, (255, 255, 255), 40), (0, 20))

            if not ((obstacle.y + GAP >= toucan.y + 40 >= obstacle.y) or (obstacle.y + GAP >= toucan.y >= obstacle.y))\
                    and (obstacle.x <= toucan.x <= obstacle.x + 80 or (obstacle.x <= toucan.x + 60 <= obstacle.x + 80)):
                reset()
                run = False
