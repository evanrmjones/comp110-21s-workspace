"""Tar Heels exercise redux as a structured program."""

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))
    

# TODO 1: Define the tar_heels function, and its logic, here.
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
