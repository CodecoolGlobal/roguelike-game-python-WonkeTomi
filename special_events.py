import ui
import random

GET_CHOICE = ["Yes", "No"]

FAKTOR = ["You are lucky, ", "You get fucked, "]
OUTCOME = ["You lost 20HP", "You got 20HP"]

POSSIBILITIES = {':evergreen_tree:': ["This peach is rotten inside and infested with worms.", "It was really tasty."]}
EAT_PEACH = "You have just found a shiny, juicy lookin thicc peach. Do you taste it or not?"
SAVING = "Would you like to save?"
CASTLE = "You have found an empty looking castle and though what could be inside. Would you like to look around?"
LAMA = "You have run into a cute, handsome and kind lama and thinking of petting the cutie. Do you want to pet it or not"
BANANA = "You have found a banana. Do you take it or not?"
ROLL_DIE = "You have found a magical dice. Do you wanna roll it or not? (Might something happen)"
ONION = "You have found an onion apparently there are other ingredients for a stew. Do you want to cook it or not?"
PILL = "You have just found a wierd little pill. Do you take it?"
ICE_CREAM = "You have found an ice cream and it looks like it's melting. Do you lick it off and eat it or not?"
MIDDLE_FINGER1 = "You have just found a jerk with it's middle finger up and kicked his ass. Do you take +10 attack or did it just for fun?"
MIDDLE_FINGER2 = "You have just found a jerk with it's middle finger up and he kicked your ass. It hits you with 50 damage you weak nerd."
MUSHROOM = "You have found a death cap mushroom and you are hungry. Do you eat it or not?"

events = [POSSIBILITIES, ]

def choose_special(special):
    outcome = random.randint(0, 1)
    for event in events:
        if special[2][2] == event.keys():
            print(FAKTOR[outcome])
            print(event[special[2][2]][outcome])
            print(OUTCOME[outcome])
