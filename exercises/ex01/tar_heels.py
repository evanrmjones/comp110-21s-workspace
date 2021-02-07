"""An exercise in remainders and boolean logic."""

__author__ = "730389248"


# Begin your solution here...
num: int = int(input("Enter an int: "))
if num%2 == 0 and num%7 == 0:
    print("TAR HEELS")
elif num%2 == 0: 
    print("TAR")
elif num%7 == 0: 
    print("HEELS")
else: 
    print("CAROLINA")
