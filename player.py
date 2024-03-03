import pygame

from random import randint as rand

input_blocks = [pygame.Rect( rand(100, 700), rand(50, 200), rand(100, 400), rand(50, 200) ) for i in range(10)]
block_size = 20

class Player:
    def __init__(self):

        self.colour = (50, 100, 150)
        self.width = 30
        self.height = 50
        self.dimensions = [self.width, self.height]

        self.pos = [500,300]
        self.vel = [0, 0]
        self.acc = [0, 0]

        self.walk_speed = 1.3
        self.jump_height = 14

        self.drag = 0.8

        self.controls = {'up' : pygame.K_UP,
                         'down' : pygame.K_DOWN,
                         'left' : pygame.K_LEFT,
                         'right' : pygame.K_RIGHT}
        
        self.hitbox = pygame.Rect(*self.pos, self.width, self.height)

    def update(self, keys_pressed, gravity_strength):
        #handle inputs
        self.hitbox = pygame.Rect(*self.pos, self.width, self.height)

        self.acc = [0, gravity_strength]

        if keys_pressed[self.controls['right']]:
            self.acc[0] = self.walk_speed
        if keys_pressed[self.controls['left']]:
            self.acc[0] = -self.walk_speed
        if keys_pressed[self.controls['up']] and self.pos[1] >= 400:
            self.vel[1] = -self.jump_height

        self.vel[0] *= self.drag

        self.vel = addVec(self.vel, self.acc)
        self.pos = addVec(self.pos, self.vel)

        #crude floor detection
        if self.pos[1] > 400:
            self.pos[1] = 400
            self.vel[1] = 0
            self.acc[1] = 0

        """
        for block in input_blocks:
            if True: #should be checking that blocks are close enough to be processed
                
                if self.hitbox.colliderect(block.top_hitbox) and self.vel[0] > 0:
                    self.vel[0] = 0
                    self.acc[0] = 0

                if self.hitbox.colliderect(block.bottom_hitbox) and self.vel[0] < 0:
                    self.vel[0] = 0
                    self.acc[0] = 0

                if self.hitbox.colliderect(block.left_hitbox) and self.vel[0] > 0:
                    self.vel[0] = 0

                if self.hitbox.colliderect(block.right_hitbox) and self.vel[0] > 0:
                    self.vel[0] = 0
                    """


    def draw(self, screen):
        #jank because rectangles draw from the top left
        pygame.draw.rect(screen, self.colour, [*subVec( self.pos, multVec(self.dimensions, 0.5)), *self.dimensions])

        #for block in input_blocks:
        #    pygame.draw.rect(screen, (100,0,100), block)

addVec = lambda a, b : [a[0]+b[0], a[1]+b[1]]
subVec = lambda a, b : [a[0]+b[0], a[1]+b[1]]
multVec = lambda v, c : [v[0]*c, v[1]*c]