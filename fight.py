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


def attack_menu(room):
    pos = 0
    buttons = ["Attack", "Defend", "Item"]
    while isinstance(pos, int):
        pos = ui.button_system(buttons, pos, attack_phase_control)
    calc_damage(characters.main_character, room[2][2], pos)


def calc_damage(character, enemy, fight_type):
    if enemy in engine.MOBS[1]:
        enemy = characters.mobs[engine.MOBS[1].index(enemy)]
    elif enemy in engine.BOSS[1]:
        enemy = characters.bosses[engine.BOSS[1].index(enemy)]
    atk_modifier = 1.0
    def_modifier = 1.0
    luck = 0.5 + random.random()
    if luck > 1:
        print("Lucky!")
    else:
        print("Unlucky...")
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
        enemy_display = enemy["EMOJI"]
        print(f"You attacked {enemy_display} and dealt {damage} damage.")
    elif fight_type == "defense":
        if character["ATK"] > enemy["ATK"] and character["DEF"] > enemy["DEF"]:
            def_modifier *= 1.25
        elif character["ATK"] < enemy["ATK"] and character["DEF"] < enemy["DEF"]:
            def_modifier *= 0.75
        elif enemy["HP"] > 20:
            def_modifier *= 1.1
        def_modifier += luck / 2
        resistance = round(character["DEF"] * def_modifier) - enemy["ATK"]
        print(resistance)


def use_inventory(character):
    pass


if __name__ == "__main__":
    while characters.CROCODILE["HP"] > 0:
        calc_damage(characters.main_character, characters.CROCODILE, "attack")
    attack_menu(engine.create_room(random.choice(engine.MOBS[0]), countain_of_room=random.choice(engine.MOBS[1])))