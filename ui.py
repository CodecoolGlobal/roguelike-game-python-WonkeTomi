from copy import copy
import emoji
from util import clear_screen, key_pressed
import time
import engine
import ui


MENU_BUTTONS = ["New Game", "Continue", "I'm too weak, so I Quit"]


def print_error_message(message):
    print("ERROR: {message}")


def display_intro():
    print(''' 

                Welcome to Word of Zsa!

             The magical word of randomness

                        made by:

                    Zsa - like game    

        Dávid, SzimBensze, Tomi, Poga, MiMi, Zoty           
    
    ''')
    time.sleep(5)
    clear_screen()


def display_title():
    
    print('''
        ▄▄▌ ▐ ▄▌      ▄▄▄  ▄▄▌  ·▄▄▄▄            ·▄▄▄    ·▄▄▄▄•.▄▄ ·  ▄▄▄· 
        ██· █▌▐█▪     ▀▄ █·██•  ██▪ ██     ▪     ▐▄▄·    ▪▀·.█▌▐█ ▀. ▐█ ▀█ 
        ██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ██▪  ▐█· ▐█▌     ▄█▀▄ ██▪     ▄█▀▀▀•▄▀▀▀█▄▄█▀▀█ 
        ▐█▌██▐█▌▐█▌.▐▌▐█•█▌▐█▌▐▌██. ██     ▐█▌.▐▌██▌.    █▌▪▄█▀▐█▄▪▐█▐█ ▪▐▌
        ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀.▀▀▀ ▀▀▀▀▀•      ▀█▄▀▪▀▀▀     ·▀▀▀ • ▀▀▀▀  ▀  ▀ 
    ''')


def display_button(buttons):
    for button in buttons:
        print(f"\n {button.center(80)}")


def create_button(buttons, pos):
    symbol_right = ' <-'
    symbol_left = '-> '
    buttons_to_create = copy(buttons)
    buttons_to_create[pos] = symbol_left + buttons_to_create[pos] + symbol_right
    return buttons_to_create


def print_menu():
    pos = 0
    while True:
        clear_screen()
        ui.display_title()
        buttons = ui.create_button(ui.MENU_BUTTONS, pos)
        ui.display_button(buttons)
        pos = ui.change_button_pos(pos, buttons)
        

def change_button_pos(pos, buttons):
    key = key_pressed()
    if key == 's':
        if pos < len(buttons) - 1:
            pos += 1
    elif key == 'w':
        if pos > 0:
            pos -= 1
    return pos


def change_menu(button):
    if button == 0:
        print("yep")
    elif button == 1:
        print_error_message("Not implemented yet")
    elif button == 2:
        quit()


def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''

    NUMBER_OF_ROWS_OF_ROOMS = 4
    NUMBER_OF_ROWS_IN_A_ROOM = 5
    NUMBER_OF_ROOMS_IN_A_ROW = 4
    NUMBER_OF_CELLS_IN_A_ROW_IN_A_ROOM = 5

    for room_row in range(NUMBER_OF_ROWS_OF_ROOMS):
        for room_lines in range(NUMBER_OF_ROWS_IN_A_ROOM):
            for room in range(NUMBER_OF_ROOMS_IN_A_ROW):
                for room_cells in range(NUMBER_OF_CELLS_IN_A_ROW_IN_A_ROOM):
                    current_room = (room_row*4)+room
                    cell_to_print = board[current_room][room_lines][room_cells]
                    if len(cell_to_print) == 1:
                        print(cell_to_print, end='')
                    else:
                        print(emoji.emojize(cell_to_print), end='')
                print('  ', end='')
            print()
        print()


if __name__ == '__main__':
    board = engine.create_board()
    display_board(board)
