import random

name = 'BlackJack'

cards = {
    'Ace of Spades': (1, 11),
    '2 of Spades': (2,),
    '3 of Spades': (3,),
    '4 of Spades': (4,),
    '5 of Spades': (5,),
    '6 of Spades': (6,),
    '7 of Spades': (7,),
    '8 of Spades': (8,),
    '9 of Spades': (9,),
    '10 of Spades': (10,),
    'Jack of Spades': (10,),
    'Queen of Spades': (10,),
    'King of Spades': (10,),    
    'Ace of Club': (1, 11),
    '2 of Club': (2,),
    '3 of Club': (3,),
    '4 of Club': (4,),
    '5 of Club': (5,),
    '6 of Club': (6,),
    '7 of Club': (7,),
    '8 of Club': (8,),
    '9 of Club': (9,),
    '10 of Club': (10,),
    'Jack of Club': (10,),
    'Queen of Club': (10,),
    'King of Club': (10,),    
    'Ace of Hearts': (1, 11),
    '2 of Hearts': (2,),
    '3 of Hearts': (3,),
    '4 of Hearts': (4,),
    '5 of Hearts': (5,),
    '6 of Hearts': (6,),
    '7 of Hearts': (7,),
    '8 of Hearts': (8,),
    '9 of Hearts': (9,),
    '10 of Hearts': (10,),
    'Jack of Hearts': (10,),
    'Queen of Hearts': (10,),
    'King of Hearts': (10,),    
    'Ace of Diamonds': (1, 11),
    '2 of Diamonds': (2,),
    '3 of Diamonds': (3,),
    '4 of Diamonds': (4,),
    '5 of Diamonds': (5,),
    '6 of Diamonds': (6,),
    '7 of Diamonds': (7,),
    '8 of Diamonds': (8,),
    '9 of Diamonds': (9,),
    '10 of Diamonds': (10,),
    'Jack of Diamonds': (10,),
    'Queen of Diamonds': (10,),
    'King of Diamonds': (10,),    
}

def get_new_deck():
    deck = []

    # add 4 decks of cards
    deck.extend(cards.keys())
    deck.extend(cards.keys())
    deck.extend(cards.keys())
    deck.extend(cards.keys())

    random.shuffle(deck)
    return deck

def deal_game():
    player_hand = []
    dealer_hand = []

    deck = get_new_deck()

    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    return deck, dealer_hand, player_hand

def calculate_hand(hand):
    totals = [0]
    for card_name in hand:
        new_totals = []        
        for total_index in range(0, len(totals)):
            total = totals[total_index]
            for value in cards[card_name]:
                new_totals.append(total + value)
        totals = new_totals

    # convert to a set and back to a list to remove duplicates
    return list(set(totals))

def is_busted(values):
    busted = True
    for value in values:
        if value < 21:
            busted = False
            break
    return busted

def play_game():
    deck, dealer, player = deal_game()

    player_turn = True

    while True:
        dealer_values = calculate_hand(dealer)
        player_values = calculate_hand(player)
        print('Dealer:')
        print(dealer)
        print(dealer_values)
        print('Player:')
        print(player)
        print(player_values)
        
        if 21 in dealer_values and 21 in player_values:
            print('Tie')
            break

        if 21 in dealer_values:
            print('Dealer wins :(')
            break

        if 21 in player_values:
            print('Blackjack!')
            break

        player_bust = is_busted(player_values)

        if player_bust:
            print('Bust - you lose :(')
            break

        dealer_bust = is_busted(dealer_values)

        if dealer_bust:
            print('Dealer bust')
            break

        if player_turn:
            hit = ''
            while hit != 'y' and hit != 'n':
                hit = input('Hit (y/n)? ').strip().lower()

            if hit == 'y':
                player.append(deck.pop())
            else:
                player_turn = False
        else:
            stand_values = [val for val in dealer_values if 17 <= val <= 21]
            if not stand_values:
                print('Dealer hits')
                dealer.append(deck.pop())
            else:
                dealer_score = max([v for v in dealer_values if v <= 21])
                player_score = max([v for v in player_values if v <= 21])
                if dealer_score == player_score:
                    print('Tie')
                elif player_score > dealer_score:
                    print('Player wins!')
                else:
                    print('Dealer wins')
                break


    print('Game Over')


if __name__ == "__main__":
    play_game()