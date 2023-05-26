import pygame
from pygame.locals import *
import random

pygame.init()

bgFile = pygame.image.load("Assets/oceanBG.png")
fishFiles = [pygame.image.load("Assets/Fish0.png"), pygame.image.load("Assets/Fish1.png"), pygame.image.load("Assets/Fish2.png"),
             pygame.image.load("Assets/Fish3.png"), pygame.image.load("Assets/Fish4.png"), pygame.image.load("Assets/Fish5.png")]

bite = pygame.mixer.Sound("Assets/Munch.wav")
music = pygame.mixer.Sound("Assets/Sharkio-Track.wav")
death = pygame.mixer.Sound("Assets/Sharkio-Death.wav")

win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Shark.io")
clock = pygame.time.Clock()


def text(t, c, size):
    font = pygame.font.SysFont("Noteworthy", size)
    t = font.render(t, True, c)
    return t


class PlayerFish:
    def __init__(self):
        self.fishNum = 1
        self.fish = fishFiles[self.fishNum]
        self.size = 0
        self.x = 0
        self.y = 0
        self.living = True
        self.level = 1
        self.currLevel = 0

    def collision(self, food):
        if food < self.fishNum:
            bite.play()
            if food == 0:
                self.size += 1
                self.currLevel += 1
            if food == 1:
                self.size += 2
                self.currLevel += 2
            if food == 2:
                self.size += 5
                self.currLevel += 5
            if food == 3:
                self.size += 10
                self.currLevel += 10
            if food == 4:
                self.size += 15
                self.currLevel += 15
            if self.fishNum == 5 and self.currLevel >= 50:
                self.currLevel = 0
                self.levelUp()
        if food >= self.fishNum:
            music.stop()
            death.play()
            self.living = False

    def levelUp(self):
        if self.fishNum == 4:
            self.currLevel = 0
        if self.fishNum < 5:
            self.fishNum += 1
        self.fish = fishFiles[self.fishNum]
        self.level += 1


class Enemy:
    def __init__(self, x, y, fishNum):
        self.x = x
        self.y = y
        self.fishType = fishNum
        self.speed = random.randint(1, 7)

    def move(self):
        self.x -= self.speed

    def reset(self):
        self.x = random.randint(1000 + 25 * self.fishType, 2500)
        self.y = random.randint(0, 600 - 25 * self.fishType)
        self.fishType = random.randint(0, 5)
        self.speed = random.randint(1, 7) + player.level


enemies = []
for i in range(10):
    enemies.append(Enemy(random.randint(600, 1000) * i, random.randint(0, 600), (i % 6)))


run = True
mainMenu = True
gameRun = False
endScreen = False
instructionScreen = False
tickNum = 0
secs = 0
enemyNum = 0

player = PlayerFish()

music.play(-1)

# Main loop
while run:
    # Main Menu
    while mainMenu:

        pygame.display.update()
        pygame.mouse.set_visible(False)
        player.x, player.y = pygame.mouse.get_pos()
        clock.tick(120)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                mainMenu = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                run = False
                mainMenu = False
            if event.type == KEYDOWN and event.key == K_RETURN:
                gameRun = True
            if event.type == MOUSEBUTTONDOWN and 580 >= player.x >= 345 and 189 <= player.y <= 280:
                gameRun = True
            if event.type == MOUSEBUTTONDOWN and 684 >= player.x >= 242 and 309 <= player.y <= 400:
                instructionScreen = True
        win.fill((0, 0, 0))
        win.blit(bgFile, (0, 0))
        win.blit(player.fish, (player.x, player.y))

        # Text
        win.blit(text("Shark.io", (210, 158, 99), 150), (273, -35))
        win.blit(text("PLAY", (210, 158, 99), 100), (382, 170))
        win.blit(text("Instructions", (210, 158, 99), 100), (279, 290))

        if 580 >= player.x >= 345 and 189 <= player.y <= 280:
            win.blit(text("PLAY", (0, 0, 0), 100), (382, 170))
        if 684 >= player.x >= 242 and 309 <= player.y <= 400:
            win.blit(text("Instructions", (0, 0, 0), 100), (279, 290))

        # Instruction Screen
        while instructionScreen:
            pygame.display.update()
            pygame.mouse.set_visible(False)
            player.x, player.y = pygame.mouse.get_pos()
            clock.tick(60)

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    mainMenu = False
                    instructionScreen = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    run = False
                    mainMenu = False
                    instructionScreen = False
            win.fill((0, 0, 0))
            win.blit(bgFile, (0, 0))
            win.blit(player.fish, (player.x, player.y))

            # Instruction Text


        # In Game
        while gameRun:
            pygame.display.update()
            pygame.mouse.set_visible(False)
            player.x, player.y = pygame.mouse.get_pos()
            clock.tick(60)

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    mainMenu = False
                    gameRun = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    run = False
                    mainMenu = False
                    gameRun = False
                if event.type == KEYDOWN and event.key == K_SPACE:
                    player.levelUp()
            win.fill((0, 0, 0))
            win.blit(bgFile, (0, 0))
            win.blit(player.fish, (player.x, player.y))

            if player.size < 100:
                win.blit(text("Score: " + str(player.size), (210, 158, 99), 100), (600, -35))
            if player.size >= 100:
                win.blit(text("Score: " + str(player.size), (210, 158, 99), 100), (530, -35))
            if player.fishNum == 1:
                nextL = 5
            elif player.fishNum == 2:
                nextL = 20
            elif player.fishNum == (3 or 5):
                nextL = 50
            elif player.fishNum == 4:
                nextL = 100
            else:
                nextL = 0

            win.blit(text("LevelUp: ", (210, 158, 99), 50), (15, 0))
            pygame.draw.rect(win, (0, 0, 0), Rect(175, 25, 250, 50))
            pygame.draw.rect(win, (210, 158, 99), Rect(175, 25, (250 - (nextL - player.currLevel) * 250 / nextL), 50))

            # Blitting and testing collisions
            for enemy in enemies:
                win.blit(pygame.transform.flip(fishFiles[enemy.fishType], True, False), (enemy.x, enemy.y))
                enemy.move()
                if enemy.x < -50 - 100 * enemy.fishType:
                    enemy.reset()

                if player.x < enemy.x < (player.x + (25 * player.fishNum) + 25) and player.y < enemy.y < player.y + 25:
                    player.collision(enemy.fishType)
                    enemies.remove(enemy)
                    enemies.append(Enemy(random.randint(1000, 2000), random.randint(0, 500), random.randint(0, 5)))

            # Leveling Up
            if 5 <= player.size < 20 and player.level == 1:
                player.levelUp()
            if 20 <= player.size < 50 and player.level == 2:
                player.levelUp()
            if 50 <= player.size < 100 and player.level == 3:
                player.levelUp()
            if 100 <= player.size and player.level == 4:
                nextLevelUp = 100
                currLevelSize = 0
                player.levelUp()

            if not player.living:
                print("Dead")
                endScreen = True
                gameRun = False

        while endScreen:
            print("Game Over")
            print(player.size)
            break


pygame.quit()
