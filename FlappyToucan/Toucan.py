class Toucan:

    def __init__(self, x, y, vel, state):
        self.x = x
        self.y = y
        self.vel = vel
        self.state = state

    def fly_up(self):
        self.vel = -15

    def gravity(self):
        self.y += self.vel
        self.vel += 1
