import pygame

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
RECTANGLE_HEIGHT = WINDOW_HEIGHT / 3

ARMENIA_FLAG_COLORS = ('#D90012', '#0033A0', '#F2A800')
BULGARIA_FLAG_COLORS = ('#FFFFFF', '#009B74', '#D01C1F')
YEMEN_FLAG_COLORS = ('#CE1126', '#FFFFFF', '#000000')

top_rectangle = pygame.Rect((0, 0), (WINDOW_WIDTH, RECTANGLE_HEIGHT))
mid_rectangle = pygame.Rect((0, RECTANGLE_HEIGHT), (WINDOW_WIDTH, RECTANGLE_HEIGHT))
bottom_rectangle = pygame.Rect((0, 2*RECTANGLE_HEIGHT), (WINDOW_WIDTH, RECTANGLE_HEIGHT))

# increment by one every time we draw the animation.
# Based on the number, we choose which flag to display
counter = 0
top_color, mid_color, bottom_color = ARMENIA_FLAG_COLORS

# pygame set up.
pygame.init()
pygame.display.set_caption('flags animation')
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# How many seconds to wait before updating the screen
update_rate = 1

while True:
    time_delta = clock.tick(update_rate)

    if counter % 3 == 0:
        top_color, mid_color, bottom_color = ARMENIA_FLAG_COLORS
    if counter % 3 == 1:
        top_color, mid_color, bottom_color = BULGARIA_FLAG_COLORS
    if counter % 3 == 2:
        top_color, mid_color, bottom_color = YEMEN_FLAG_COLORS

    pygame.draw.rect(window_surface, top_color, top_rectangle)
    pygame.draw.rect(window_surface, mid_color, mid_rectangle)
    pygame.draw.rect(window_surface, bottom_color, bottom_rectangle)

    counter += 1
    pygame.display.update()
