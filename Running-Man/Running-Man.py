import pygame
from pygame.locals import *
import random

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Running Man')

bg = pygame.image.load('Assets/Running_Man_Background.jpg')

clock = pygame.time.Clock()

running_sprites = [pygame.image.load('Assets/Running_Man_Pos0.png'),
                   pygame.image.load('Assets/Running_Man_Pos1.png'),
                   pygame.image.load('Assets/Running_Man_Pos2.png'),
                   pygame.image.load('Assets/Running_Man_Pos3.png'),
                   pygame.image.load('Assets/Running_Man_Pos4.png'),
                   pygame.image.load('Assets/Running_Man_Pos5.png'),
                   pygame.image.load('Assets/Running_Man_Pos6.png'),
                   pygame.image.load('Assets/Running_Man_Pos7.png')]


obstacle_sprites = [pygame.transform.flip((pygame.image.load('Assets/Doggo.png')), True, False),
                    pygame.transform.flip((pygame.image.load('Assets/bunny.png')), True, False),
                    pygame.transform.flip((pygame.image.load('Assets/Red_Thing.png')), True, False),
                    pygame.transform.flip((pygame.image.load('Assets/Pig.png')), True, False),
                    pygame.transform.flip((pygame.image.load('Assets/Cat.png')), True, False)]

pygame.mixer.music.load('Assets/Action_Fighter.wav')

explosion = pygame.mixer.Sound('Assets/Explosion.wav')

pygame.mixer.music.play(-1)


def text(t, c, size):
    font = pygame.font.SysFont('arial', size)
    t = font.render(t, True, c)
    return t


running_sprite_num = 0
counter_num = 0
obstacle_num = 0


bg_x = 0

game_speed = 7
player_run_speed = 10
dist_num = 550
game_mult = 1.1

player_height = 75
player_width = 50
player_x = 50
player_y = 355 - player_height
player_y_vel = 0

obstacle1_x = -100
obstacle2_x = -100
obstacle3_x = -100

obstacle1 = obstacle_sprites[random.randint(0, 4)]
obstacle2 = obstacle_sprites[random.randint(0, 4)]
obstacle3 = obstacle_sprites[random.randint(0, 4)]

main_menu = True
end_screen = False

while main_menu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            main_menu = False

    pygame.display.update()

    clock.tick(144)

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, ((bg_x + 800), 0))
    bg_x -= game_speed
    if bg_x < -800:
        bg_x = 0

    screen.blit(running_sprites[running_sprite_num], (player_x, player_y))

    if counter_num % 50 == 0:
        obstacle_num = random.randint(0, 4)

    counter_num += 1
    if counter_num % player_run_speed == 0:
        running_sprite_num += 1
        if running_sprite_num > 7:
            running_sprite_num = 0

    player_y_vel -= 1
    obstacle1_x -= game_speed
    obstacle2_x -= game_speed
    obstacle3_x -= game_speed

    screen.blit(obstacle1, (obstacle1_x, 305))
    screen.blit(obstacle2, (obstacle2_x, 305))
    screen.blit(obstacle3, (obstacle3_x, 305))

    if not player_y == (355 - player_height):
        player_y -= player_y_vel

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and player_y == (355 - player_height):
        player_y_vel = 15
        player_y -= player_y_vel

    random_num = random.randint(0, 100)

    if (random_num < 3) and (obstacle1_x < -50)\
            and not (dist_num < obstacle2_x < 800) and not (dist_num < obstacle3_x < 800):
        obstacle1 = obstacle_sprites[(random.randint(0, 4))]
        obstacle1_x = 800

    if 3 <= random_num < 5 and (obstacle2_x < -50)\
            and not (dist_num < obstacle1_x < 800) and not (dist_num < obstacle3_x < 800):
        obstacle2 = obstacle_sprites[(random.randint(0, 4))]
        obstacle2_x = 800

    if 5 <= random_num < 7 and (obstacle3_x < -50)\
            and not (dist_num < obstacle1_x < 800) and not (dist_num < obstacle2_x < 800):
        obstacle3 = obstacle_sprites[(random.randint(0, 4))]
        obstacle3_x = 800

    if (0 < obstacle1_x < 125) and (player_y > 230):
        pygame.mixer.Sound.play(explosion)
        end_screen = True

    if (0 < obstacle2_x < 125) and (player_y > 230):
        pygame.mixer.Sound.play(explosion)
        end_screen = True

    if (0 < obstacle3_x < 125) and (player_y > 230):
        pygame.mixer.Sound.play(explosion)
        end_screen = True

    if counter_num % 250 == 0:
        game_speed *= game_mult
        dist_num /= game_mult
        if player_run_speed > 1:
            player_run_speed -= 1

    screen.blit(text(('Score: %s' % counter_num), (0, 0, 0), 50), (600, 50))

    while end_screen:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu = False
                end_screen = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                main_menu = False
                end_screen = False
            if event.type == KEYDOWN and event.key == K_SPACE:
                obstacle1_x = -100
                obstacle2_x = -100
                obstacle3_x = -100
                counter_num = 0
                game_speed = 7
                player_run_speed = 10
                dist_num = 550
                end_screen = False

        screen.fill(0)
        screen.blit(bg, (0, 0))

        screen.blit(text('Nice Playing!', (0, 0, 0), 50), (282, 100))
        screen.blit(text(('Score: %s' % counter_num), (0, 0, 0), 50), (322, 200))

pygame.quit()
