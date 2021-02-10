"""Tar Heels exercise redux as a structured program."""

__author__ = "730389248"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))
    

def tar_heels(num: int) -> str: 
    if num % 2 == 0 and num % 7 == 0:
       return "TAR HEELS"
    elif num % 2 == 0: 
        return "TAR"
    elif num % 7 == 0: 
        return "HEELS"
    else: 
        return "CAROLINA"


if __name__ == "__main__":
    main()
