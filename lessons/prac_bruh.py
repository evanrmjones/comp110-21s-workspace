word: str = "hello"


new_word: str = ""


for i in range(0, len(word)): 
    new_word = (new_word + word[(len(word) -1) - i])
print(word + new_word)