heyy: str = "hello"

"""
for i in range(0, len(heyy)):
    new_word: str = (heyy[(len(heyy)-1) - i])
    print(new_word)
"""

new_word: str = ""
for i in range(0, len(heyy)): 
    new_word = heyy + (heyy[(len(heyy)-1) - i]
print(new_word)