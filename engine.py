import random
from tkinter import BOTTOM
from xml.dom.pulldom import CHARACTERS
import emoji
import characters
import os
import ui
import characters

from util import key_pressed

ITEMS_DICT = {':anatomical_heart:': 'H25', ':sushi:':'H20', ':Christmas_tree:':'A3', ':baby_bottle:':'H10', ':magic_wand:':'A20', ':dagger:':'A10', 'crossed_swords':'A20', 'water_pistol':'A5', ':bomb:': 'A23', ':shield:':'D30', ':blue_square:':'D5'}
NORMAL_ITEMS = [':brick:', list(ITEMS_DICT)]
SPECIAL_EVENTS = [[':deciduous_tree:', ':evergreen_tree:'], [':house:', ':floppy_disk:'], [':hut:', ':castle:'], [':wood:', ':llama:'], [':rolling_on_the_floor_laughing:', ':banana:'], [':shuffle_tracks_button:', ':game_die:'], [':salt:', ':zebra:'], [':wood:', ':onion:'], [':sandwich:', ':pill:'], [':shallow_pan_of_food:', ':salt:'], [':face_savoring_food:', ':soft_ice_cream:'], [':palms_up_together:', ':middle_finger:'], [':wood:', ':mushroom:']]
MOBS = [[':rock:', ':zany_face:'], [":vampire:", ":crocodile:", ":skunk:", ":butterfly:", ":clown_face:", ":dodo:", ":mosquito:", ":zombie:"]]
BOSS = [[':fire:', ':skull:', ':fearful_face:'], [":Russia:", ":T-Rex:", ":laptop:"]]
EMPTY_ROOM = [':butter:', ':fuel_pump:', ':collision:']
FLOOR = ':black_large_square:'
DOOR = ':door:'

TOP = (1,2)
BOTTOM = (3,2)
LEFT = (2,1)
RIGHT = (2,3)
PLAYER_ICON = characters.main_character['EMOJI']


def create_room(wall_elements, countain_of_room=FLOOR, door=DOOR):
    first_last_row = [wall_elements, wall_elements, door, wall_elements, wall_elements]
    second_forth_row = [wall_elements, FLOOR, FLOOR, FLOOR, wall_elements]
    third_row = [door, FLOOR, countain_of_room, FLOOR, door]
    whole_room = []
    whole_room.append(first_last_row)
    for i in range(3):
        if i == 1:
            whole_room.append(third_row)
        else:
            whole_room.append(second_forth_row)
    whole_room.append(first_last_row)
    return whole_room


def create_board(width=4, height=4):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    full_room_count = width * height
    room = []
    for items in range(2):
        room.append(create_room(NORMAL_ITEMS[0], countain_of_room=random.choice(NORMAL_ITEMS[1])))
    for special in range(2):
        random_special = random.choice(SPECIAL_EVENTS)
        room.append(create_room(random_special[0], random_special[1]))
    for mobs in range(2):
        room.append(create_room(random.choice(MOBS[0]), countain_of_room=random.choice(MOBS[1])))
    room.append(create_room(random.choice(BOSS[0]), countain_of_room=random.choice(BOSS[1])))
    room.append(create_room(random.choice(EMPTY_ROOM), countain_of_room=characters.main_character["EMOJI"]))
    actual_room_count = len(room)
    while full_room_count > actual_room_count:
        room.append(create_room(random.choice(EMPTY_ROOM)))
        actual_room_count = actual_room_count + 1
        random.shuffle(room)
    return room


def put_player_on_board(board, room, placement):
    # Modifies the game board by placing the player icon at its coordinates.
    board[room][placement[0]][placement[1]] = PLAYER_ICON
    

def search_and_clear_player(board):
    NUMBER_OF_ROWS_OF_ROOMS = 4
    NUMBER_OF_ROWS_IN_A_ROOM = 5
    NUMBER_OF_ROOMS_IN_A_ROW = 4
    NUMBER_OF_CELLS_IN_A_ROW_IN_A_ROOM = 5

    for room_row in range(NUMBER_OF_ROWS_OF_ROOMS):
        for room_lines in range(NUMBER_OF_ROWS_IN_A_ROOM):
            for room in range(NUMBER_OF_ROOMS_IN_A_ROW):
                for room_cells in range(NUMBER_OF_CELLS_IN_A_ROW_IN_A_ROOM):
                    current_room = (room_row*4)+room
                    cell_to_check = board[current_room][room_lines][room_cells]
                    if cell_to_check == PLAYER_ICON:
                        board[current_room][room_lines][room_cells] = FLOOR
                        return current_room


def character_movement(board):
    ESC = chr(27)

    current_room = search_and_clear_player(board)
    game_over = False
    while not game_over:
        ui.display_board(board)
        control_key = key_pressed()
        if control_key == ESC:
            game_over = True
        elif control_key == 'w':
            put_player_on_board(board, current_room-4, BOTTOM)

        elif control_key == 's':
            pass
        elif control_key == 'a':
            pass
        elif control_key == 'd':
            pass


'''def create_new_player():
    valid_name = False
    while not valid_name:
        player_name = "./player/"
        player_name += input(" Please give me your character name: ")
        player_name += ".txt"
        if os.path.exists(player_name):
            ui.print_error_message("Player name is already taken choose another one!")
        else:
            with open(player_name,'w') as file:
                file.write('''

if __name__ == "__main__":
    # for i in range(len(create_room('#', countain_of_room='8'))):
    #     print(create_room('#', countain_of_room='8')[i])
    
    board = create_board()
    character_movement(board)
        