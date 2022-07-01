from copyreg import dispatch_table
import util
import engine
import ui
import emoji
import json


def before_game():
    # ui.display_intro()
    ui.print_menu()


def start_the_game():
    engine.character_movement(engine.create_board())


def main():
    before_game()
    start_the_game()


if __name__ == '__main__':
    main()