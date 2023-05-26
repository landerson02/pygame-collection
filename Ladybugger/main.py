import pygame
from pygame.locals import *
import Ladybug
import Images
import Vehicles
import random

# Game Constants and Variables
WIDTH = 560
HEIGHT = 640

score = 0
level = 1

main_menu = True
run = False
end_screen = False

lanes = []
for lane in range(12):
    lanes.append(lane * 40 + 80)

# Basic functions


def text(t, c, size):
    font = pygame.font.SysFont("arial", size)
    t = font.render(t, True, c)
    return t


pygame.init()
ladybug = Ladybug.Lbug(160, 600)
cars = []

for i in range(12):
    cars.append(Vehicles.Car(random.randint(60, 500), lanes[i], bool(i % 2), random.randint(0, 5)))

# window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ladybugger")
clock = pygame.time.Clock()

# Main loop
while main_menu:
    pygame.display.update()
    pygame.mouse.set_visible(True)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(mouse_x, mouse_y)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            main_menu = False
        if event.type == MOUSEBUTTONDOWN:
            run = True
        if event.type == KEYDOWN and event.key == K_SPACE:
            run = True
    win.fill((0, 0, 0))
    win.blit(Images.bg_file, (0, 0))
    # win.blit(text("Ladybugger", (255, 0, 0), 100), (10, 50))
    win.blit(text("Press space to play!", (50, 50, 150), 50), (65, 525))

    while run:
        clock.tick(30)

        Vehicles.car_vel = level

        pygame.display.update()
        pygame.mouse.set_visible(False)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu = False
                run = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                main_menu = False
                run = False
            if event.type == KEYDOWN and event.key == K_UP:
                ladybug.move_up()
                score += 1
            if event.type == KEYDOWN and event.key == K_DOWN:
                ladybug.move_down()
                score -= 1
            if event.type == KEYDOWN and event.key == K_LEFT:
                ladybug.move_left()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                ladybug.move_right()

        win.fill((0, 0, 0))
        for i in range(8):
            win.blit(Images.road_file, (0, (HEIGHT - 80 * i)))
        for i in range(4):
            win.blit(Images.grass_file, (((i - 1) * 200), 560))
            win.blit(Images.grass_file, (((i - 1) * 200), 0))
        win.blit(text("score:%s" % score, (0, 0, 0), 50), (20, 20))
        win.blit(text("Level:%s" % level, (0, 0, 0), 50), (370, 20))

        win.blit(Images.ladybug_file, (ladybug.x, ladybug.y))

        for car in cars:

            win.blit(Images.car_files[car.car_num], (car.x, car.lane))

            car.move()

            # Collisions
            if (car.x <= ladybug.x + 20 <= car.x + 100 or car.x <= ladybug.x <= car.x + 100) and ladybug.y == car.lane:
                end_screen = True
            if ladybug.y <= 40:
                ladybug.y = 600
                level += 1
                for a in cars:
                    if a.car_num < 5:
                        a.car_num += 1
                    a.x = random.randint(0, 500)

        while end_screen:
            pygame.display.update()
            pygame.mouse.set_visible(True)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # print(mouse_x, mouse_y)

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu = False
                    run = False
                    end_screen = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    main_menu = False
                    run = False
                    end_screen = False
                if event.type == KEYDOWN and event.key == K_SPACE:
                    ladybug.y = 600
                    ladybug.x = 160
                    score = 0
                    level = 1
                    end_screen = False
            win.fill((0, 0, 0))
            for i in range(3):
                for j in range(16):
                    win.blit(Images.grass_file, (200 * i, 40 * j))
            win.blit(text("Game Over :(", (255, 255, 255), 75), (95, 100))
            win.blit(text("Score: %s" % score, (255, 255, 255), 75), (100, 250))
            win.blit(text("Level: %s" % level, (255, 255, 255), 75), (100, 400))
            win.blit(text("[Space to play again!]", (255, 255, 255), 30), (100, 500))


pygame.quit()
