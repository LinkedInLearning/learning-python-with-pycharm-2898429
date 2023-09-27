import pygame
import pygame_gui


class EventController:
    def __init__(self, start: pygame_gui.elements.UIButton, next: pygame_gui.elements.UIButton, reset: pygame_gui.elements.UIButton):
        self.start_button = start
        self.next_button = next
        self.reset_button = reset

    def assess(self, event, state):
        if event.type == pygame.QUIT:
            return handle_quit(state)

        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_button:
                return handle_start_pause(state, event.ui_element)
            if event.ui_element == self.reset_button:
                return handle_reset(state, self.start_button)
            if event.ui_element == self.next_button:
                return handle_next(state, self.start_button)
            else:
                return {}

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return handle_grid_click(state)

        return {}


def handle_quit(state):
    state['is_running'] = False
    return state


def handle_reset(state, start_button):
    state['grid'].reset()
    state['animation_running'] = False
    start_button.set_text('Start')

    pygame.mixer.music.load('./sound_effects/reset.mid')
    pygame.mixer.music.play()

    return state


def handle_start_pause(state, button):
    state['animation_running'] = not state['animation_running']
    button.set_text('Pause') if state['animation_running'] else button.set_text('Start')
    return state


def handle_grid_click(state):
    pos = pygame.mouse.get_pos()
    state['grid'].check_clicks(pos)
    return {}


def handle_next(state, start_button):
    state['grid'].update()
    state['animation_running'] = False
    start_button.set_text('Start')
    return {}
