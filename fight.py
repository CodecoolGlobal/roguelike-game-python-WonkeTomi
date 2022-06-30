import characters
import events
import random


def attack_phase():
    pass


def attack_menu():
    pass


def calc_damage(character, enemy, fight_type):
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
        atk_modifier *= luck
        damage = round(character["ATK"] * atk_modifier) - enemy["DEF"]
        if damage <= 0:
            damage = 1
        enemy["HP"] -= damage
        print(enemy)
    elif fight_type == "defense":
        if character["ATK"] > enemy["ATK"] and character["DEF"] > enemy["DEF"]:
            def_modifier *= 1.25
        elif character["ATK"] < enemy["ATK"] and character["DEF"] < enemy["DEF"]:
            def_modifier *= 0.75
        elif enemy["HP"] > 20:
            def_modifier *= 1.1
        def_modifier *= luck
        resistance = round(character["DEF"] * def_modifier) - enemy["ATK"]
        print(resistance)


def use_inventory(character):
    pass


if __name__ == "__main__":
    while characters.CROCODILE["HP"] > 0:
        calc_damage(characters.main_character, characters.CROCODILE, "attack")