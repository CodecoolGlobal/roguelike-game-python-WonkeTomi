import random
import emoji

NORMAL_ITEMS = [':brick:', [':anatomical_heart:', ':Christmas_tree:', ':baby_bottle:', ':magic_wand:']]
SPECIAL_EVENTS= [[':deciduous_tree:', ':evergreen_tree:'], [':house:', ':floppy_disk:'], [':hut:', ':castle:'], [':wood:', ':llama:'], [':rolling_on_the_floor_laughing:', ':banana:'], [':shuffle_tracks_button:', ':game_die:'], [':salt:', ':zebra:'], [':wood:', ':onion:'], [':sandwich:', ':pill:'], [':shallow_pan_of_food:', ':salt:'], [':face_savoring_food:', ':soft_ice_cream:'], [':palms_up_together:', ':middle_finger:'], [':wood:', ':mushroom:']]
MOB_WALL = [':rock:', ':zany_face:']
BOSS_WALL = [':fire:', ':skull:', ':fearful_face:']
EMPTY_ROOM = [':butter:', ':fuel_pump:', ':collision:']


def create_room(wall_elements, countain_of_room = ':black_large_square:', door = ':door:'):
    first_last_row = [wall_elements, wall_elements, door, wall_elements, wall_elements]
    second_forth_row = [wall_elements, ':black_large_square:', ':black_large_square:', ':black_large_square:', wall_elements]
    third_row = [door, ':black_large_square:', countain_of_room, ':black_large_square:', door]
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
        room.append(create_room(random.choice(MOB_WALL), countain_of_room=emoji.emojize(':nazar_amulet:')))
    room.append(create_room(random.choice(BOSS_WALL), countain_of_room=emoji.emojize(':bikini:')))
    room.append(create_room(random.choice(EMPTY_ROOM), countain_of_room=emoji.emojize(':tongue:')))
    actual_room_count = len(room)
    while full_room_count > actual_room_count:
        room.append(create_room(random.choice(EMPTY_ROOM)))
        actual_room_count = actual_room_count + 1
    return room


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass

if __name__ == "__main__":
    # for i in range(len(create_room('#', countain_of_room='8'))):
    #     print(create_room('#', countain_of_room='8')[i])
    board = create_board()
    for room in board:
        for line in room:
            print(*line)
        print()
        