import pygame
import pygame_gui

from grid import Grid
from controller import EventController

GAME_BACKGROUND_COLOR = '#0F0F00'
UI_BACKGROUND_COLOR = '#FFFFFF'

pygame.init()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 650
UI_HEIGHT = 130

GAME_HEIGHT = WINDOW_HEIGHT - UI_HEIGHT

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40

GAME_BACKGROUND_COLOR = '#000000'
UI_BACKGROUND_COLOR = '#000000'

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

game_background = pygame.Surface((WINDOW_WIDTH, GAME_HEIGHT))
game_background.fill(pygame.Color(GAME_BACKGROUND_COLOR))

ui_background = pygame.Surface((WINDOW_WIDTH, UI_HEIGHT))
ui_background.fill(pygame.Color(UI_BACKGROUND_COLOR))

manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

manager.preload_fonts([{'name': 'fira_code', 'point_size': 14, 'style': 'bold'}])

start_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((70, GAME_HEIGHT + 30), (BUTTON_WIDTH, BUTTON_HEIGHT)),
                text='Start',
                tool_tip_text='Start or Pause the simulation',
                manager=manager)

reset_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((2*70 + BUTTON_WIDTH, GAME_HEIGHT + 30), (BUTTON_WIDTH, BUTTON_HEIGHT)),
                text='Reset',
                tool_tip_text='Clear all cells from the screen',
                manager=manager)

next_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((3*70 + 2*BUTTON_WIDTH, GAME_HEIGHT + 30), (BUTTON_WIDTH, BUTTON_HEIGHT)),
            text='Next',
            tool_tip_text='Move the simulation one step forward then pause it',
            manager=manager)

rules_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((4*70 + 3*BUTTON_WIDTH, GAME_HEIGHT + 30), (BUTTON_WIDTH, BUTTON_HEIGHT)),
            text='Rules',
            tool_tip_text='<b>Rule 1:</b> Any active cell with two or three live neighbours survives.<br><b>Rule 2: </b>Any inactive cell with three live neighbours becomes active.<br><b>Rule 3:</b> All other active cells die in the next generation.',
            starting_height=7,
            manager=manager)

shapes_selector = pygame_gui.elements.UIDropDownMenu(['glider', 'pentadecathlon', 'lightweight'],
                                                     'glider',
                                                     relative_rect=pygame.Rect((5*70+4*BUTTON_WIDTH, GAME_HEIGHT + 30), (BUTTON_WIDTH*2, BUTTON_HEIGHT)),
                                                     manager=manager)

g = Grid((WINDOW_WIDTH, GAME_HEIGHT), window_surface, 20, 15)
g.insert_shape('glider')

clock = pygame.time.Clock()

game_state = {'is_running': True, 'animation_running': False, 'grid': g}
controller = EventController(start=start_button, next=next_button, reset=reset_button, shapes=shapes_selector)

pygame.mixer.music.load("./sound_effects/intro.mid")

def display(state):
    window_surface.blit(game_background, (0, 0))
    window_surface.blit(ui_background, (0, GAME_HEIGHT))

    if state['animation_running']:
        state['grid'].update()

    state['grid'].draw(window_surface)
    manager.draw_ui(window_surface)
    pygame.display.update()


pygame.mixer.music.play()
while game_state['is_running']:

    current_grid = game_state['grid']
    time_delta = clock.tick(5) / 1000.0
    for event in pygame.event.get():
        # pass the event and the game state to the controller
        # controller figures out what kind of event to address
        # updates the game state accordingly
        updated_state = controller.assess(event, game_state)
        game_state.update(updated_state)

        manager.process_events(event)

    manager.update(time_delta)
    display(game_state)

