import random
import time


def ai_move(myboard):
    print("Get AI move")
    while True:
        choice = random.randrange(0, 8, 1)
        if myboard[choice].isspace():
            print("Dokonano ruchu")
            return choice


def get_user_move(myboard):
    options = [0,1,2,3,4,5,6,7,8]
    print("Where do you want to execute move?")
    print("0   1   2")
    print("3   4   5")
    print("6   7   8")

    start = time.time()
    while (time.time() - start) < 5:
        while True:
            choice = int(input("Insert number from 0 to 8"))
            if choice in options:
                break
            else:
                print("Choose number from 0 to 8")
        if myboard[choice].isspace():
            print("Dokonano ruchu")
            return choice
        else:
            print("Ta część planszy jest już zajęta")

    if choice is None:
        print("Czas na wprowadzenie wartości minął.")
        return None



def is_player_starting():
    print("Orzeł czy reszka?")
    choice = int(input("Orzeł(0) czy reszka(1)?"))
    which = random.randint(0, 1)
    if which==0:
        if choice==0:
            print("Orzeł! Zaczynasz")
            return True
        else:
            print("Reszka! Zaczyna przeciwnik")
            return False
    else:
        if choice==0:
            print("Orzeł! Zaczyna przeciwnik")
            return False
        else:
            print("Reszka! Zaczynasz")
            return True
