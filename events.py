import characters
import engine
import emoji
import special_events
import ui
import fight


def check_event(room):
    if event_die(characters.main_character) != None:
        return "You died!"
    room_item = room[2][2]
    if room_item in engine.ITEMS_DICT.keys():
        event_item({room_item: engine.ITEMS_DICT[room_item]})
    elif room_item in engine.MOBS[1]:
        event_fight(characters.main_character, characters.mobs[engine.MOBS[1].index(room_item)], room)
    elif room_item in engine.BOSS[1]:
        event_fight(characters.main_character, characters.bosses[engine.BOSS[1].index(room_item)], room)
    elif room_item in [item[1] for item in engine.SPECIAL_EVENTS]:
        event_special(characters.main_character, room)
    else:
        return "This is an empty room."


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
            print("Mana item picked up! (WIP)")
    return character


def event_item(item, message='You found an item.'):
    for _, value in item.items():
        if value[0] == "A" or value[0] == "D":
            characters.main_character["INVENTORY"].update(item)
        else:
            characters.main_character["BAG"].update(item)
    return characters.main_character


def event_fight(character, enemy, room):
    ui.clear_screen()
    check_hp = fight.check_hp(character, enemy)
    while check_hp == None:
        character, enemy = fight.attack_menu(room)
        check_hp = fight.check_hp(character, enemy)
    if check_hp == "win":
        ui.print_message([event_win(character, enemy)])
    elif check_hp == "die":
        ui.print_message([event_die(character)])
    return characters.main_character


def event_special(character, room):
    ui.clear_screen()
    ui.print_room(room)
    special_events.choose_special(character, room)


def event_win(character, enemy):
    enemy_name = emoji.demojize(enemy["EMOJI"])
    if enemy["HP"] <= 0:
        return f"You defeated {enemy_name[1:-1]}! Good job!"
    else:
        return None


def event_die(character):
    if character["HP"] <= 0:
        return "You died! RIP"
    else:
        return None


if __name__ == "__main__":
    #characters.CROCODILE["HP"] = 0
    # print(event_win(characters.main_character, characters.SKUNK))
    # print(event_die(characters.main_character, characters.SKUNK))
    # event_item({':dagger:':'A10'})
    # event_item({':baby_bottle:':'H10'})
    # print(characters.main_character["BAG"])
    # check_item(characters.main_character)
    # print(characters.main_character)
    event_fight(characters.main_character, characters.CROCODILE, engine.create_room(engine.MOBS[0], engine.MOBS[1][0]))