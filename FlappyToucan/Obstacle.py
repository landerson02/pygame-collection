import random


class Obstacle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x -= 5

    def new_y(self):
        self.y = random.randint(100, 550)
