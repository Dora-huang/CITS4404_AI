import pygame
from random import randint, uniform, random
import math
from time import time, sleep

# This is a 2-Dimensional vector
vector = pygame.math.Vector2
# the stride for each step
gravity = vector(0, 0.3)
# the canvas width and height
WIDTH = HEIGHT = 600

class Particle:
    '''
    initial the single particle for fireworks
    if firework status is 1 that means particle upward, otherwise scattered particles
    '''
    def __init__(self, x, y, status, colour):
        self.status = status
        self.ori_pos = vector(x, y) # original postition
        self.pos = vector(x, y) # current postition
        self.remove = False 
        self.explosion_radius = randint(7, 20)
        self.life = 0
        # upward
        if self.status == 1:
            self.vel = vector(0, -randint(15, 18))
            self.size = 5
            self.colour = colour
        # scatter
        else:
            self.vel = vector(uniform(-1, 1), uniform(-1, 1))
            self.vel.x *= randint(7, self.explosion_radius+1)
            self.vel.y *= randint(7, self.explosion_radius+1)
            self.size = 2
            self.colour = colour

    def move(self, force):
        '''
        reduce the stride and change particles position based on firework status
        '''
        if self.status == 0:
            self.vel.x *= 0.8
            self.vel.y *= 0.8

        self.vel += force
        self.pos += self.vel

        self.decay()
        self.life += 1

    def decay(self):
        '''
        calculate the likelihood of dacay based on particles' life
        '''
        if 10 < self.life < 50:
            dead = random()
            if dead < 0.2:
                self.remove = True
        elif self.life > 50:
            dead = random()
            if dead > 0.5:
                self.remove = True


class Firework:

    def __init__(self):
        '''
        initial the single upward particle and exploded status
        '''
        self.colour = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.particle = Particle(randint(0, WIDTH), HEIGHT, 1, self.colour)
        self.exploded = False
        self.particles = []

    def update(self, win):
        '''
        if the status is upward: when it achieves the top, the status changes to scatter
        and randomly choose the number of particles, otherwise the particle already exploded
        '''
        if not self.exploded:
            pygame.draw.circle(win, self.colour, (int(self.particle.pos.x), int(self.particle.pos.y)), 
                                self.particle.size)
            self.particle.move(gravity)
            #print(self.particle.pos, self.particle.vel)
            if self.particle.vel.y >= 0:
                self.exploded = True
                amount = randint(100,200) 
                for i in range(amount):
                    self.particles.append(Particle(self.particle.pos.x, self.particle.pos.y, 0, self.colour))
        else:
            for ptl in self.particles:
                ptl.move(vector(gravity.x + uniform(-1, 1) / 20, gravity.y + random()))
                #print(ptl.pos, ptl.vel)
                pygame.draw.circle(win, self.colour, (int(ptl.pos.x), int(ptl.pos.y)), 
                                ptl.size)
        

    def remove(self):
        '''
        remove the dead particles
        and only when particles list is empty
        remove the whole firework
        '''
        if self.exploded:
            for ptl in self.particles:
                if ptl.remove is True:
                    self.particles.remove(ptl)

            if len(self.particles) == 0:
                return True
            else:
                return False


def UpdateFirws(win, fireworks):
    for fw in fireworks:
        fw.update(win)
        if fw.remove() is True:
            fireworks.remove(fw)
            # print("remove fw sucessfully")
    pygame.display.update()


def Game():
    # create a dynamic fireworks list which can increase or delete elements during the loop
    fireworks = [Firework() for i in range(3)]
    # initial the game
    pygame.init()
    # the screen of game
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    # set a clock
    clock = pygame.time.Clock()

    # starting the game
    aa = True
    while aa:
        clock.tick(30)
        win.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aa = False

        if random() < 0.05:
            fireworks.append(Firework())
        UpdateFirws(win, fireworks)
    
    pygame.quit()
    quit()

Game()