import random

car_vel = 1


class Car:

    def __init__(self, x, lane, d, car_num):
        self.x = x
        self.lane = lane
        self.car_num = car_num
        self.d = d

    def move(self):

        if self.d:
            self.x += car_vel
            if self.x >= 560:
                self.x = 0
                self.car_num = random.randint(0, 5)

        if not self.d:
            self.x -= car_vel
            if self.x <= 00:
                self.x = 540
                self.car_num = random.randint(0, 5)
