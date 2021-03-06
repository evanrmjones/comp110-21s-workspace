"""EX03 - palindromify function."""


__author__: str = "YOUR PID HERE"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    print(palindromify("race", False)) 
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))
   

def palindromify(word: str, even_or_odd: bool) -> str: 
    """Makes a palindrome."""
    new_word: str = ""
    if even_or_odd == True: 
        for letter in range(0, len(word)): 
            new_word = new_word + word[(len(word)-1) - letter]
    else: 
        for letter in range(0, (len(word) - 1)): 
            new_word = new_word + word[(len(word)-2) - letter]
    return word + new_word


if __name__ == "__main__":
    main()