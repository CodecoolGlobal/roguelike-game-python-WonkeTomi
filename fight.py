import characters
import events
import ui
import engine
import random


def attack_phase_control(button):
    if button == 0:
        return "attack"
    elif button == 1:
        return "defense"
    elif button == 2:
        return "item"


def check_hp(character, enemy):
    if character["HP"] < 0:
        return "die"
    elif enemy["HP"] < 0:
        return "win"
    else:
        return None


def attack_menu(room):
    pos = 0
    buttons = ["Attack", "Defend", "Item"]
    while isinstance(pos, int):
        pos = ui.button_system(buttons, pos, attack_phase_control)
    character_updated, enemy_updated = calc_damage(characters.main_character, room[2][3], pos)
    return character_updated, enemy_updated


def calc_damage(character, enemy_display, fight_type):
    print_messages = []
    if enemy_display in engine.MOBS[1]:
        enemy = characters.mobs[engine.MOBS[1].index(enemy_display)]
    elif enemy_display in engine.BOSS[1]:
        enemy = characters.bosses[engine.BOSS[1].index(enemy_display)]
    
    atk_modifier, def_modifier = 1.0, 1.0
    luck = 0.5 + random.random()
    resistance = 1
    enemy_emoji = enemy["EMOJI"]

    if luck > 1:
        print_messages.append("Lucky!")
    else:
        print_messages.append("Unlucky...")
    if fight_type == "attack":
        if character["ATK"] > enemy["ATK"] and character["DEF"] > enemy["DEF"]:
            atk_modifier *= 1.25
        elif character["ATK"] < enemy["ATK"] and character["DEF"] < enemy["DEF"]:
            atk_modifier *= 0.75
        elif enemy["HP"] < 20:
            atk_modifier *= 1.1
        atk_modifier += luck / 2
        damage = round(character["ATK"] * atk_modifier) - enemy["DEF"]
        if damage <= 0:
            damage = 1
        enemy["HP"] -= damage
        print_messages.append(f"You attacked {enemy_emoji} and dealt {damage} damage.")
    elif fight_type == "defense":
        if character["ATK"] > enemy["ATK"] and character["DEF"] > enemy["DEF"]:
            def_modifier *= 1.25
        elif character["ATK"] < enemy["ATK"] and character["DEF"] < enemy["DEF"]:
            def_modifier *= 0.75
        elif enemy["HP"] > 20:
            def_modifier *= 1.1
        def_modifier += luck / 2
        resistance = round(character["DEF"] * def_modifier) - enemy["ATK"]
        if resistance < 5:
            resistance = 5
        print_messages.append(f"You defended yourself and absorbed {resistance} damage.")
    elif fight_type == "item":
        print_messages.append("Sorry this feature is WIP.")
        return character, enemy
    if enemy["ATK"] > character["ATK"]:
        enemy_atk_modifier = 1.1
    else:
        enemy_atk_modifier = 0.8
    enemy_dmg = enemy["ATK"] * enemy_atk_modifier - resistance
    if enemy_dmg < 1:
        enemy_dmg = 1
    character["HP"] -= round(enemy_dmg)
    print_messages.append(f"{enemy_display} hit you and you lost {enemy_dmg} HP.")
    ui.print_message(print_messages)
    return character, enemy


def use_inventory(character):
    print("WIP")


if __name__ == "__main__":
    #while characters.CROCODILE["HP"] > 0:
    #    calc_damage(characters.main_character, characters.CROCODILE, "attack")
    #random_room_for_testing = engine.create_room(random.choice(), random.choice(engine.MOBS[1]))
    attack_menu(engine.create_room(engine.MOBS[0],engine.MOBS[1][1]))