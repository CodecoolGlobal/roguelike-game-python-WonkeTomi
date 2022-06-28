import emoji
from util import clear_screen, key_pressed
import time
import msvcrt


def display_room(room):
    pass


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

        if msvcrt.getch().decode('utf-8') == 's':
            if button_pos >= 0:
                button_pos -= 1
        elif msvcrt.getch().decode('utf-8') == 'w':
            if button_pos <= 0:
                button_pos += 1
        elif msvcrt.getch().decode('utf-8') == ' ':
            return button_pos
            
        

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
                print(' ', end='')
            print()
        print()



print(emoji.emojize(":1st_place_medal:"))

board = []
for i in range(16):
    room = []
    for n in range(5):
        room_line = []
        for y in range(5):
            room_line.append('w')
        room.append(room_line)
    board.append(room)

display_board(board)