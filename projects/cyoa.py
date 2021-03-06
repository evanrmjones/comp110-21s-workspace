"""A coin flipping simulation game that tells you how many coin flips you guess in a row."""


import random 


POINTS_CONSTANT: int = 1 
flip_list: list[str] = ["heads", "tails"]
points: int 
game_over: bool 
player: str


def main() -> None: 
    """The main function."""
    global points
    global game_over
    game_over = False
    points = 0 
    greet()
    while game_over != True: 
        action: str = input("what would you like to do ")
        if action == "guess": 
            guess: str = input("heads or tails? ")
            print(rand_guess(guess))
        elif action == "quit":
            print(f"you finished with {points} points")
            game_over = True 
        elif action == "display":
            print(f"you currently have {points} points")
    return None


def greet() -> None: 
    """Greets player."""
    global player
    player = input("What is your name? ")
    print(f"Welcome {player} to a game where you have to guess a coin flips result. For every one you get right, you get one point. Use the display command to see how many points you have. When you are done playing the game, use the quit command to conclude the game. ")
    return None 


def rand_flip(list: list[str]) -> str: 
    """Flips coin randomly."""
    index_list: int = random.randint(0, 1)
    return list[index_list]


def rand_guess(guess: str) -> str: 
    """Determines if guess is correctly."""
    global flip_list
    global points
    if guess == rand_flip(flip_list):
        points += POINTS_CONSTANT 
        return f"Good job! you guessed correctly! \U0001F973" 
    else: 
        points = 0  
        return f"Sorry {player}, you guessed incorrectly, try again. \U0001F614"


if __name__ == "__main__":
    main()