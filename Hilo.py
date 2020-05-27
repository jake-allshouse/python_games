
name = 'High/Low'

def play_game():
    low = 1
    high = 1000

    print("Please think of a number between {} and {}".format(low, high))
    print("I will guess your number in 10 guesses")
    input("Press ENTER to start")

    guesses = 1
    while True:
        guess = low + (high - low) // 2
        high_low = input("My guess is {}. Should I guess higher or lower? "
                        "Enter h or l, or c if my guess was correct "
                        .format(guess)).casefold()
        
        if high_low == "h":
            # Guess higher. The low end of the range becomes 1 greater than the guess.
            low = guess + 1
            guesses += 1
        elif high_low == "l":
            # Guess lower. The high end of the range becomes 1 less than the guess.
            high = guess - 1
            guesses += 1
        elif high_low == "c":
            print("I got it in {} guesses!".format(guesses))
            break
        else:
            print("Please enter h, l, or c")
            

    if guesses <= 10:
        print("I win!")
    else:
        print("I did not guess in 10 guesses. You win!")

if __name__ == "__main__":
    play_game()