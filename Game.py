import random


def ask():
    print("Do you want to play a game?")
    a = input("Y/N ")
    if a.strip().upper() == "Y":
        print("Good!")
        return "Let's play!"
    elif a.strip().upper() == "N":
        print("Fine be that way!")
        return "Bye"
    else:
        print("What did you say?")
        return None


def guessing_game():
    number = random.randint(1, 100)
    gotit = False
    while not gotit:
        print("I'm thinking of a number between 1 and 100")
        guess = int(input())
        print(guess)
        if guess == number:
            print("Great job!")
            gotit = True
        elif guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print("Something went wrong")


def gameloop():

    answer = ask()
    while not answer:
        answer = ask()

    if answer == "Let's play!":
        guessing_game()
    print("Goodbye")

gameloop()
