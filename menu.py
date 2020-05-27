import BlackJack
import get2048
import Hilo
import Madlibs
import numberGuess
import slotmachine

games = [BlackJack, get2048, Hilo, Madlibs, numberGuess, slotmachine]

def run_menu():
    counter = 0
    print('Choose a game:')    
    for game in games:
        counter += 1
        print('{}. {}'.format(counter, game.name))
        
    game_index = 0
    while not game_index:
        try:
            game_index = int(input('Choose a game number? '))
            if game_index < 1 or game_index > len(games):
                game_index = 0
        except ValueError:
            pass # they must not have typed a number
    
    games[game_index - 1].play_game()

if __name__ == "__main__":
    run_menu()