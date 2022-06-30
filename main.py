from copyreg import dispatch_table
import util
import engine
import ui
import emoji


def before_game():
     ui.display_intro()
     ui.print_menu()

def main():
    before_game()
    

if __name__ == '__main__':
     ui.print_menu()