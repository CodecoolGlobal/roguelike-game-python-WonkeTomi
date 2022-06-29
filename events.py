import characters
import emoji


def check_event(item_type):
    pass


def check_item(item):
    pass


def event_item(item, message):
    pass


def event_fight(character, enemy):
    pass


def event_special(spec, decisions):
    pass


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
    print(event_win(characters.main_character, characters.CROCODILE))
    print(event_die(characters.main_character, characters.CROCODILE))