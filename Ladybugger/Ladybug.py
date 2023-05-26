# Ladybug

move_distance = 20


class Lbug:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y -= 40

    def move_down(self):
        if self.y <= 640 - 2 * move_distance:
            self.y += 40

    def move_left(self):
        if self.x >= move_distance:
            self.x -= move_distance

    def move_right(self):
        if self.x <= 560 - 2 * move_distance:
            self.x += move_distance
