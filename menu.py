import os

import common

# these are the games
import BlackJack
import get2048
import Hilo
import Madlibs
import numberGuess
import slotmachine

games = [BlackJack, get2048, Hilo, Madlibs, numberGuess, slotmachine]

def clear_screen():
    os.system('cls')  # For Windows
    #os.system('clear')  # For Linux/OS X

def run_menu():
    counter = 0
    print('Choose a game:')    
    for game in games:
        counter += 1
        print('{}. {}'.format(counter, game.name))
        
    game_number = 0
    while not game_number:
        try:
            game_number = int(input('Choose a game number? '))
            if game_number < 1 or game_number > len(games):
                game_number = 0
        except ValueError:
            pass # they must not have typed a number
    
    return game_number - 1
    

def menu_loop():
    while True:
        clear_screen()
        game_index = run_menu()
        clear_screen()
        games[game_index].play_game()        

        play_another = common.get_answer('Play another game (y/n)? ', ('y', 'n'))
        if play_another == 'n':
            break


if __name__ == "__main__":
    menu_loop()