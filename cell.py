import pygame
from pygame.locals import Rect

INACTIVE_COLOR = "#16302B"
ACTIVE_COLOR = "#C0E5C8"


class Cell(Rect):
    def __init__(self, pos: tuple, dimensions: tuple, active=False):
        self.active = active
        self.future_state = None

        super().__init__(pos, dimensions)

    def draw(self, surface):
        """
            This method checks what state the cell is in, and draws it in the appropriate color on the provided surface
        """
        color = ACTIVE_COLOR if self.active else INACTIVE_COLOR
        return pygame.draw.rect(surface, color, self)

    def __str__(self):
        return "X" if self.active else "_"

    def flip(self):
        self.active = not self.active

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False

    def set_future_state(self, living_neighbors: int):
        if self.active and (living_neighbors == 2 or living_neighbors == 3):
            self.future_state = True
        elif not self.active and living_neighbors == 3:
            self.future_state = True
        else:
            self.future_state = False

    def update(self):
        self.active = self.future_state
        self.future_state = None
