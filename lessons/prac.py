








""" A coin flip game that guesses how many coin flip guesses you guess correctly"""
import random 


def main() -> None: 
    greet()
    guess_function()
    return None


def greet() -> None: 
    global player 
    print(f"Welcome {player} to a game where you have to guess a coin flips result. For every one you get right, you get one point. When you are done playing the game, use the quit command to conclude the game. ")


POINTS_INCR: int = 1 

points: int = 0 
heads_or_tails: list[str]
heads_or_tails = ["heads", "tails"]
flip: int = random.randint(1,2)
player: str = input("What is your name? ")

def rand_flip(flip: int) -> str: 
    flip_list_index: str = heads_or_tails[flip]
    return flip_list_index


def guess_function() -> str: 
    global heads_or_tails
    global points 
    global rand_flip
    guess: str = "null"
    while guess != "quit": 
        guess: str = input("heads or tails? ")
        if guess == rand_flip(flip): 
            points += POINTS_INCR 
            return f"good job! you guessed correctly! \U0001F973"
        else: 
            return f"sorry {player}, you guessed incorrectly, try again. \U0001F614"



if __name__ == "__main__":
    main()


