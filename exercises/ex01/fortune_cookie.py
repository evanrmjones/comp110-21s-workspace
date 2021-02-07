"""Program that outputs one of at least four random, good fortunes."""

__author__ = 730389248

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

"""
cookie_bank: list = ["A beautiful, smart, and loving person will be coming into your life." , "Your life will be happy and peaceful." , "Soon life will become more interesting.", "Success lies in the hands of those who wants it.]
print("Your fortune cookie says...")
print(cookie_bank[randint(0,3)])
print("Now, go spread positive vibes!")
"""

print("Your fortune cookie says...")
rand_num: int = randint(0,3)
if rand_num == 0:
    print("A beautiful, smart, and loving person will be coming into your life.")
elif rand_num == 1:
    print("Your life will be happy and peaceful.")
elif rand_num == 2:
    print("Soon life will become more interesting.")
elif rand_num == 3: 
    print("Success lies in the hands of those who wants it.")
print("Now, go spread positive vibes!")