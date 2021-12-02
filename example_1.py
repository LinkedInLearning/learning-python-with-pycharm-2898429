a1 = '#D90012'
b1 = '#0033A0'
c1 = '#F2A800'
a2 = '#FFFFFF'
b2 = '#009B74'
c2 = '#D01C1F'
a3 = '#CE1126'
b3 = '#FFFFFF'
c3 = '#000000'
import pygame

x = pygame.Rect((0, 0), (600, 300))
pygame.init()
y =pygame.Rect((0, 100), (600, 300))

window_surface= pygame.display.set_mode((1200, 600))
z = pygame.Rect((0, 200), (600, 300))

token = 0



while True:
    time_delta = pygame.time.Clock().tick(1)
    if token % 3 == 0: a,b,c=a1,b1,c1

    if token % 3 == 1: a, b, c = a2, b2, c2
    if token % 3 == 2: a,b, c= a3,b3, c3

    pygame.draw.rect(window_surface,a, x)
    pygame.draw.rect(window_surface, b,y)

    pygame.draw.rect(window_surface,c,z)

    token = token + 1
    pygame.display.update()



