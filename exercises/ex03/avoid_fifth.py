"""EX03 - avoid_fifth function."""


__author__: str = "730389248"


e_list: list[str] = ["e", "E"]
#empty: list[str] = []


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore"))
    return None


def avoid_fifth(word: str) -> str: 
    """Function that parses a string and determines if it has the letter "E" and removes it. """
    new_word: str = ""
    for letter in word:  
        if letter not in e_list:
           new_word = new_word + letter 
    return new_word
   

if __name__ == "__main__":
    main()