import emoji
from util import clear_screen, key_pressed
import time



def display_room(room):
    pass

def print_error_message(message):
    print(message)

def display_intro():
    print(''' 

                Welcome to Word of Zsa!

             The magical word of randomness

                        made by:

                    Zsa - like game    

        Dávid, Szim Bence, Tomi, Poga, MiMi, Zoty           
    
    ''').center(300)
    time.sleep(5)
    clear_screen()


def display_menu():
    button_pos = 0
    while True:
        clear_screen()
        print('''
            ▄▄▌ ▐ ▄▌      ▄▄▄  ▄▄▌  ·▄▄▄▄            ·▄▄▄    ·▄▄▄▄•.▄▄ ·  ▄▄▄· 
            ██· █▌▐█▪     ▀▄ █·██•  ██▪ ██     ▪     ▐▄▄·    ▪▀·.█▌▐█ ▀. ▐█ ▀█ 
            ██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ██▪  ▐█· ▐█▌     ▄█▀▄ ██▪     ▄█▀▀▀•▄▀▀▀█▄▄█▀▀█ 
            ▐█▌██▐█▌▐█▌.▐▌▐█•█▌▐█▌▐▌██. ██     ▐█▌.▐▌██▌.    █▌▪▄█▀▐█▄▪▐█▐█ ▪▐▌
            ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀.▀▀▀ ▀▀▀▀▀•      ▀█▄▀▪▀▀▀     ·▀▀▀ • ▀▀▀▀  ▀  ▀ 
        ''')
        if button_pos == 1:
            print('                -> New game <-')
        else:
            print('                   New game  ')
        if button_pos == 0:
            print('                -> Continue <-')
        else:
            print('                   Continue  ')
        if button_pos == -1:
            print("           -> I'm WEAK, so I Quit <-")
        else:
            print("              I'm WEAK, so I Quit  ")
        letter = key_pressed()
        print(letter)
        if letter == 's':
            if button_pos >= 0:
                button_pos -= 1
        elif letter == 'w':
            if button_pos <= 0:
                button_pos += 1
        elif letter == ' ':
            changeing_menu(button_pos)


def changeing_menu(button):
    if button == 1:
        create_new_player()
    elif button == 0:
        load_player()
    elif button == -1:
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
                        print(emoji.emojize(cell_to_print))
                print('  ', end='')
            print()
        print()


if __name__ == '__main__':
    display_board(create_empty_board())
