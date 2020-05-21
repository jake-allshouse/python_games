import random

slots = ["BAR", " 7 ", " $ ", " $$", "$$$", "   ", "   "]
slots1 = slots
slots2 = slots
slots3 = slots


def slots_sample():
    col1 = random.sample(slots1, k=3)
    col2 = random.sample(slots2, k=3)
    col3 = random.sample(slots3, k=3)
    line1 = [col1[0], col2[0], col3[0]]
    line2 = [col1[1], col2[1], col3[1]]
    line3 = [col1[2], col2[2], col3[2]]
    return line1, line2, line3


def slots_game():
    print("Press ENTER to pull handle:")
    print("Type exit to leave game:")
    exit_game = False
    while not exit_game:
        l1, l2, l3 = slots_sample()
        choice = input()
        if choice == '':
            print(l1, l2, l3, sep='\n')
            continue
        elif choice == "exit":
            break


slots_game()
