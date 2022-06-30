import characters
import engine
import emoji
import special_events
import ui

def check_event(room):
    room_item = room[2][2]
    if room_item in engine.ITEMS_DICT.keys():
        event_item({room_item: engine.ITEMS_DICT[room_item]})
    elif room_item in engine.MOBS[1]:
        event_fight(characters.main_character, characters.mobs[engine.MOBS[1].index(room_item)])
    elif room_item in engine.BOSS[1]:
        event_fight(characters.main_character, characters.bosses[engine.BOSS[1].index(room_item)])
    elif room_item in engine.SPECIAL_EVENTS:
        event_special(characters.main_character, room_item)
    else:
        return f"This is an empty room."


def check_item(character):
    for key, value in character["BAG"].items():
        item_type = value[0]
        item_value = int(value[1:])
        if item_type == "A":
            character["ATK"] += item_value
        elif item_type == "D":
            character["DEF"] += item_value
        elif item_type == "H":
            character["HP"] += item_value
        elif item_type == "M":
            pass
    return character


def event_item(item, message='You found an item.'):
    
    for _, value in item.items():
        if value[0] == "A" or value[0] == "D":
            characters.main_character["INVENTORY"].update(item)

        else:

            characters.main_character["BAG"].update(item)

    return characters.main_character


def event_fight(character, enemy):
    print(enemy)
    pass


def event_special(character, special):
    if special == ':evergreen_tree:':
        
    


def event_win(character, enemy):
    character
    enemy_emoji = enemy["EMOJI"]
    congrats = emoji.emojize(":clapping_hands:")
    if enemy["HP"] <= 0:
        return f"You defeated {enemy_emoji}! Good job! {congrats}"
    else:
        return None


def event_die(character, enemy):
    enemy_emoji = enemy["EMOJI"]
    tomb = emoji.emojize(":latin_cross:")
    if character["HP"] <= 0:
        return f"You died by {enemy_emoji}. RIP {tomb}"
    else:
        return None


if __name__ == "__main__":
    #characters.CROCODILE["HP"] = 0
    print(event_win(characters.main_character, characters.SKUNK))
    print(event_die(characters.main_character, characters.SKUNK))
    event_item({':dagger:':'A10'})
    event_item({':baby_bottle:':'H10'})
    print(characters.main_character["BAG"])
    check_item(characters.main_character)
    print(characters.main_character)