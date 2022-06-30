from copy import copy
import emoji
from util import clear_screen, key_pressed
import time
import engine
from os import system
import characters

MENU_BUTTONS = ["New Game", "Continue", "I'm too weak, so I Quit"]


def print_error_message(message):
    print(f"ERROR: {message}")
    time.sleep(1)


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


def display_buttons(buttons):
    for button in buttons:
        print(f"\n {button.center(80)}")


def create_buttons(buttons, pos):
    symbol_right = ' <-'
    symbol_left = '-> '
    buttons_to_create = copy(buttons)
    buttons_to_create[pos] = symbol_left + buttons_to_create[pos] + symbol_right
    return buttons_to_create


def change_button_pos(pos, buttons, menu_options):
    key = key_pressed()
    if key == 's':
        if pos < len(buttons) - 1:
            pos += 1
    elif key == 'w':
        if pos > 0:
            pos -= 1
    elif key == ' ':
        return menu_options(pos)
    return pos


def change_main_menu(button):
    if button == 0:
        characters.give_name_to_char(get_input("Plese type the name of your char: "))
        return "quit"
    elif button == 1:
        print_error_message("Not implemented yet")
    elif button == 2:
        quit()


def button_system(buttons, pos, menu_options):
    created_buttons = create_buttons(buttons, pos)
    display_buttons(created_buttons)
    pos = change_button_pos(pos, buttons, menu_options)
    return pos


def print_menu():
    pos = 0
    while isinstance(pos, int):
        clear_screen()
        display_title()
        pos = button_system(MENU_BUTTONS, pos, change_main_menu)


def get_input(message):
    return input(message)


def print_info():
    print('\n--> Press WSAD to move <--   --> Press ESC to quit <--')


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

    clear_screen()

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

    print_info()


def print_message(message):
    length = len(message)
    message_board = [(length + 4) * '-', '|' + (length + 2) * ' ' + '|', '|' + ' ' + message + ' ' + '|', '|' + (length + 2) * ' ' + '|', (length + 4) * '-' ]
    for row in message_board:
        print(row)


if __name__ == '__main__':
    # board = engine.create_board()
    # display_board(board)
    print_message('Ohh no! You are dead! Just inside.')