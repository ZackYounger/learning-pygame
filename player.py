import pygame

class Player:
    def __init__(self):

        self.colour = (50, 100, 150)
        self.width = 30
        self.height = 50
        self.dimensions = [self.width, self.height]

        self.pos = [500,300]
        self.vel = [0, 0]
        self.acc = [0, 0]

        self.walk_speed = 2
        self.jump_height = 10

        self.drag = 0.8

        self.controls = {'up' : pygame.K_UP,
                         'down' : pygame.K_DOWN,
                         'left' : pygame.K_LEFT,
                         'right' : pygame.K_RIGHT}

    def update(self, keys_pressed, gravity_strength):
        #handle inputs
        self.acc = [0, gravity_strength]

        if keys_pressed[self.controls['right']]:
            self.acc[0] = self.walk_speed
        if keys_pressed[self.controls['left']]:
            self.acc[0] = -self.walk_speed
        if keys_pressed[self.controls['up']] and self.pos[1] >= 500:
            self.vel[1] = -self.jump_height

        #crude floor detection
        if self.pos[1] > 400:
            self.pos[1] = 400
            self.vel[1] = 0
            self.acc[1] = 0

        self.vel[0] *= self.drag

        self.vel = addVec(self.vel, self.acc)
        self.pos = addVec(self.pos, self.vel)

    def draw(self, screen):
        #jank because rectangles draw from the top left
        pygame.draw.rect(screen, self.colour, [*subVec( self.pos, multVec(self.dimensions, 0.5)), *self.dimensions])


addVec = lambda a, b : [a[0]+b[0], a[1]+b[1]]
subVec = lambda a, b : [a[0]+b[0], a[1]+b[1]]
multVec = lambda v, c : [v[0]*c, v[1]*c]