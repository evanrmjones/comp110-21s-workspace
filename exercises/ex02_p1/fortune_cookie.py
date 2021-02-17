"""Fortune cookie exercise redux as a structured program."""


from random import randint


__author__ = "730389248"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")
    return None


def fortune_cookie() -> str:
    rand_num: int = randint(0, 3)
    if rand_num == 0:
        return "A beautiful, smart, and loving person will be coming into your life."
    elif rand_num == 1:
        return "Your life will be happy and peaceful."
    elif rand_num == 2:
        return "Soon life will become more interesting."
    elif rand_num == 3: 
        return "Success lies in the hands of those who wants it." 
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 


if __name__ == "__main__":
    main()
