import pygame
import pygame_gui


class EventController:
    def register_ui_element(self, name, element_reference):
        setattr(self, name, element_reference)

    def assess(self, event, state):
        if event.type == pygame.QUIT:
            return handle_quit(state)

        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.__getattribute__('start'):
                return handle_start_pause(state, event.ui_element)
            if event.ui_element == self.__getattribute__('reset'):
                return handle_reset(state)
            if event.ui_element == self.__getattribute__('next'):
                return handle_next(state)
            else:
                return {}

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return handle_grid_click(state)

        return {}


def handle_quit(state):
    state['is_running'] = False
    return state


def handle_reset(state):
    state['grid'].reset()
    return state


def handle_start_pause(state, button):
    state['animation_running'] = not state['animation_running']
    button.set_text('Pause') if state['animation_running'] else button.set_text('Start')
    return state


def handle_grid_click(state):
    pos = pygame.mouse.get_pos()
    state['grid'].check_clicks(pos)
    return {}


def handle_next(state):
    state['grid'].update()
    return {}