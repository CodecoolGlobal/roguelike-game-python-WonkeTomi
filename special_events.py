import ui
import random
import characters


FACTOR = ["You get fucked!", "You are lucky!"]
OUTCOME = ["You lost 20HP", "You got 20HP"]

EAT_PEACH = "You have just found a shiny, juicy lookin thicc peach."
SAVING = "You find a save icon."
CASTLE = "You have found an empty looking castle and though what could be inside. So you went inside."
LAMA = "You have run into a cute, handsome and kind looking lama and thinking of petting the cutie."
BANANA = "You have found a banana and try to eat it."
ROLL_DIE = "You have found a magical dice. You try your luck and roll the dice."
ONION = "You have found an onion apparently there are other ingredients for a stew. You cook the stew and ate it."
PILL = "You have just found a wierd little pill and eat it. Because why not."
ICE_CREAM = "You have found an ice cream looking thing. Looks like choclate one and you ate it."
MIDDLE_FINGER = "You have just found a jerk with it's middle finger up."
MUSHROOM = "You have found a little wierd mushroom. You ate it because you never learn..."
POSSIBILITIES = {
    ':evergreen_tree:': ["This peach is rotten inside and infested with worms.", "It was really tasty.", EAT_PEACH],
    ':floppy_disk:': ['There is no saving in this game.', 'There is no saving in this game but we are kind.', SAVING],
    ':castle:': ['There are some traps left in the castle and you walk into one.', 'You find some food and ate it.', CASTLE],
    ':llama:': ["The lama wasn't so happy about it so it spit at you.", 'The lama was really kind and give his flesh to you what you can eat.', LAMA],
    ':banana:': ["There are monkeys guarding their holy banana, and they attacing you.", 'It was tasty and there was no monkey nearby.', BANANA],
    ':game_die:': ['You rolled one. The dice turn into bomb and blown up.', 'You rolled 20. The dice turn into a magical frog who heals you.', ROLL_DIE],
    ':onion:': ["The onion wasn't a normal onion. It was poisionus.", 'Your belly is full.', ONION],
    ':pill:': ['At first everything seems normal. After some minutes you puke on yourself.', 'It was a C-vitamin pill. Good for you.', PILL],
    ':soft_ice_cream:': ["It wasn't choclate. It was shit...", "It was fine.", ICE_CREAM],
    ':middle_finger:': ["He just kick your ass because why not.", "You kick his ass and took his healt potion.", MIDDLE_FINGER],
    ':mushroom:': ["At first everithing seems prittier and nicer. You fellt you flying in the air. But in reallity you just halucinating and dying", "It wasn't bad.", MUSHROOM]
    }


def choose_special(character, special):
    outcome = random.randint(0, 1)
    event_index = 2
    on_goings = []
    for event in POSSIBILITIES.keys():
        if special[2][2] in event:
            on_goings.append(POSSIBILITIES[event][event_index])
            on_goings.append(FACTOR[outcome])
            on_goings.append(POSSIBILITIES[event][outcome])
            on_goings.append(OUTCOME[outcome])
            if outcome == 0:
                character["HP"] -= 20
            else:
                character["HP"] += 20
    ui.print_message(on_goings)


if __name__ == "__main__":
    choose_special(characters.main_character, [[''], [''], ["", "", ':mushroom:']])    

