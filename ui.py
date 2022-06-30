from unicodedata import name
import characters

from copy import copy
import emoji
from util import clear_screen, key_pressed
import time
import engine
from os import system
import characters
import os

MENU_BUTTONS = ["New Game", "Continue", "I'm too weak, so I Quit"]
SCREEN_ALIGNMENT = '                                    '

NUMBER_OF_ROWS_OF_ROOMS = 4
NUMBER_OF_ROWS_IN_A_ROOM = 5
NUMBER_OF_ROOMS_IN_A_ROW = 4
NUMBER_OF_CELLS_IN_A_ROW_IN_A_ROOM = 5


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
    table =[]
    table.append(['Name', 'HP', 'Attack', 'Defense', 'Experience', 'Level'])
    table.append([characters.main_character['NAME'], characters.main_character['HP'], characters.main_character['ATK'], characters.main_character['DEF'], characters.main_character['EXP'], characters.main_character['LVL']])
    print_table(table)
    print(f'{SCREEN_ALIGNMENT}--> Press WSAD to move <--   --> Press ESC to quit <--')


def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """

    number_of_columns = len(table[0])

    row_lenghts = [0 for i in range(number_of_columns)]
    
    for row in table:
        for i in range(len(row)):
            if len(str(row[i])) > row_lenghts[i]:
                row_lenghts[i] = len( str(row[i]) )
    
    total_length = 1
    for item in row_lenghts:
        total_length += (item + 3)

    v_line = ''
    for i in range(total_length+1):
        v_line += '-'

    inner_line_title = '|'
    for i in range(total_length-1):
        inner_line_title += '='
    inner_line_title += '|'

    inner_line = '|'
    for i in range(total_length-1):
        inner_line += '-'
    inner_line += '|'

    print(v_line)
    for row in range(len(table)):
        for item in range(len(table[row])):
            print_item = str(table[row][item]).center(row_lenghts[item])
            print(f'| {print_item} ', end='')
        print(' |', end='')
        if row != len(table)-1 and (row != 0):
            print(f'\n{inner_line}')
        elif row == 0:
            print(f'\n{inner_line_title}') 
    print(f'\n{v_line}')


def reposotion_player_icon(room):
    for room_lines in range(NUMBER_OF_ROWS_IN_A_ROOM):
        for room_cells in range(NUMBER_OF_CELLS_IN_A_ROW_IN_A_ROOM):
            if room[room_lines][room_cells] == engine.PLAYER_ICON:
                room[2][1] = engine.PLAYER_ICON
                room[room_lines][room_cells] = engine.FLOOR


def create_alignment(align):
    return ''.join([' 'for i in range(align)]) if (align > 0) else ''


def print_room(room):
    clear_screen()
    terminal_x, terminal_y = os.get_terminal_size()
    room[2][3] = room[2][2]
    room[2][2] = engine.FLOOR
    reposotion_player_icon(room)
    align_x_str = create_alignment((terminal_x-NUMBER_OF_ROWS_IN_A_ROOM) // 2)
    align_y_int = (terminal_y-NUMBER_OF_ROWS_IN_A_ROOM) // 2

    for i in range(align_y_int):
        print()

    for room_lines in range(NUMBER_OF_ROWS_IN_A_ROOM):
        print(align_x_str, end='')
        for room_cells in range(NUMBER_OF_CELLS_IN_A_ROW_IN_A_ROOM):
            cell_to_print = room[room_lines][room_cells]
            if len(cell_to_print) == 1:
                print(cell_to_print, end='')
            else:
                print(emoji.emojize(cell_to_print), end='')
        print()
    print()


def display_board(board): 
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''

    clear_screen()

    items = ['Your items:']


    for room_row in range(NUMBER_OF_ROWS_OF_ROOMS):
        for room_lines in range(NUMBER_OF_ROWS_IN_A_ROOM):
            print('Your items:', end='')
            print(SCREEN_ALIGNMENT, end='')
            for room in range(NUMBER_OF_ROOMS_IN_A_ROW):
                for room_cells in range(NUMBER_OF_CELLS_IN_A_ROW_IN_A_ROOM):
                    current_room = (room_row*NUMBER_OF_ROWS_OF_ROOMS)+room
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
    terminal_x, terminal_y = os.get_terminal_size()
    max_length = max([len(word) for word in message]) + 2
    print(max_length)
    print(("/" + max_length * '-' + "\\").center(terminal_x))
    for line in message:
        print(("|" + max_length * " " + '|').center(terminal_x))
        print(("|" + line.center(max_length) + "|").center(terminal_x))
    print(("|" + max_length * " " + '|').center(terminal_x))
    print(("\\" + max_length * '-' + "/").center(terminal_x))


def change_special_menu(button):
    if button == 0:
        print("yep")
    elif button == 1:
        print_error_message("Not implemented yet")


if __name__ == '__main__':
    # board = engine.create_board()
    # display_board(board)
    print_message(['Ohh no! You are dead! Just inside.', 'Oaaaaaaahh no! You are dead! Just inside.'])
