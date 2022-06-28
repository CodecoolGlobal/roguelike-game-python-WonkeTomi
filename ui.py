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
    pass
