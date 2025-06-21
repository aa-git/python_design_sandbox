import pygame
import math
import time as time_module

vel = (float)(input("enter vel(m/s): "))
theta = (float)(input("enter angle (degrees): "))
theta = theta*math.pi/180


g = 9.8 # m/s^2
dt = 0.5 # in seconds
V = 1080
H = 1920

'''
v, theta
v cos(theta)
v sin(theta)

after 't':
    x = v cos(theta) * t
    y = v sin(theta) * t - 0.5 * g * t * t

    (0,0) V x H
    x: same
    y: V - y

total time:
    0 = v sin(theta) - g t
    t = v sin(theta) / g
    total time = 2t = 2v sin(theta) /g
'''

time  = 0


pygame.init()

table = pygame.display.set_mode((V, H))
pygame.display.set_caption("projectile")
chart  = pygame.surface.Surface((V, H))
chart.fill((255,255,255))

#initialize
x,y = 0,0
sx, sy = x, V-y

while time < 2 * vel * math.sin(theta) / g:
    
    nx = vel * math.cos(theta) * (time)
    ny = vel * math.sin(theta) * time - 0.5 * g * (time ** 2)
    snx, sny = nx, V-ny

    pygame.draw.line(chart, (255,0,0), (sx, sy), (snx, sny))
    pygame.draw.circle(chart, (0,0,0), (snx, sny), 4, 2)
    chart
    table.blit(chart, (0,0))
    pygame.display.flip()
    time += dt

    sx, sy = snx, sny
    time_module.sleep(0.01)