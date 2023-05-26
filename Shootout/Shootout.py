
import pygame
from pygame.locals import *
import random

pygame.init()

alien_x = random.randint(0, 400)
alien_y = random.randint(0, 290)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Shootout')
bg = pygame.image.load('Assets/bg.jpg')
clock = pygame.time.Clock()
gunshot = pygame.mixer.Sound('Assets/gunshot.wav')
explosion_sound = pygame.mixer.Sound('Assets/Explosion.wav')
explosion_pic = pygame.image.load('Assets/Explosion.png')
music = pygame.mixer.music.load('Assets/Off_Limits.wav')


alien_sprites = [pygame.image.load('Assets/ufo_sprite1.png'),
                 pygame.image.load('Assets/ufo_sprite2.png'),
                 pygame.image.load('Assets/ufo_sprite3.png'),
                 pygame.image.load('Assets/ufo_sprite4.png'),
                 pygame.image.load('Assets/ufo_sprite5.png')]


play_color = (0, 0, 0)
timer = 0
time = 30
alien_vel = 5
score = 0
sprite_num = random.randint(0, 5)


main_menu = True
run = False
end_screen = False


def text(t, c, size):
    font = pygame.font.SysFont('arial', size)
    t = font.render(t, True, c)
    return t


pygame.mixer.music.play(-1)


while main_menu:
    if time <= 0:
        end_screen = True
        pygame.mouse.set_visible(True)
    clock.tick(60)
    pygame.display.update()
    pygame.mouse.set_visible(True)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            main_menu = False
        if event.type == MOUSEBUTTONDOWN and 180 < mouse_x < 320 and 250 < mouse_y < 320:
            sprite_num += 1
            run = True

    if 180 < mouse_x < 320 and 250 < mouse_y < 320:
        play_color = (255, 255, 255)
    else:
        play_color = (0, 0, 0)

    screen.fill(0)
    screen.blit(bg, (0, 0))
    screen.blit(text('Shootout', (0, 0, 0), 100), (100, 50))
    screen.blit(text('play', play_color, 100), (180, 250))

    screen.blit(alien_sprites[sprite_num], (alien_x, 175))

    alien_x += alien_vel
    if alien_x <= 0 or (alien_x + 100) >= 500:
        alien_vel *= -1

    while run:
        clock.tick(60)
        pygame.display.update()
        pygame.mouse.set_visible(False)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu = False
                run = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                main_menu = False
                run = False
            if event.type == MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(gunshot)

                if (alien_x <= mouse_x <= (alien_x + 100)) and ((alien_y + 48) > mouse_y > alien_y):
                    pygame.mixer.Sound.play(explosion_sound)
                    sprite_num += 1
                    if sprite_num > 4:
                        sprite_num = 0
                    score += 1
                    alien_x = random.randint(0, 400)
                    alien_y = random.randint(0, 290)

        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        screen.blit(text(('Time: %s' % time), (0, 0, 0), 50), (350, 0))
        screen.blit(text(('Score: %s' % score), (0, 0, 0), 50), (350, 50))

        screen.blit(alien_sprites[sprite_num], (alien_x, alien_y))



        alien_x += alien_vel
        if alien_x <= 0 or (alien_x + 100) >= 500:
            alien_vel *= -1

        pygame.draw.circle(screen, 0, (mouse_x, mouse_y), 50, 2)
        pygame.draw.rect(screen, 0, (mouse_x, (mouse_y - 50), 1, 100))
        pygame.draw.rect(screen, 0, ((mouse_x - 50), mouse_y, 100, 1))

        timer += 1
        if timer % 50 == 0:
            time -= 1

        if time <= 0:
            end_screen = True

        while end_screen:
            pygame.display.update()
            pygame.mouse.set_visible(True)
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_screen = False
                    run = False
                    main_menu = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    main_menu = False
                    run = False
                    end_screen = False
                if event.type == MOUSEBUTTONDOWN and 150 < mouse_x < 350 and 300 < mouse_y < 340:
                    score = 0
                    time = 30
                    end_screen = False

            screen.fill(0)
            screen.blit(bg, (0, 0))
            screen.blit(text('Nice Shooting!', (0, 0, 0), 50), (132, 50))
            screen.blit(text(('Score: %s' % score), (0, 0, 0), 50), (172, 150))
            screen.blit(text('Play Again?', play_color, 50), (150, 300))

            if 150 < mouse_x < 350 and 300 < mouse_y < 340:
                play_color = (255, 255, 255)
            else:
                play_color = (0, 0, 0)


pygame.quit()
