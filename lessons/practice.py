""""

string: str = "string"
print(string[1])
empty: list[str] = []
empty.append(string[1])
empty.append(string[2])
print(empty[0] + empty[1])


word: str = "hello"
e_list: list[str] = ["e", "E"]
empty_list: list[str] = []

for letter in word: 
    if letter not in e_list: 
        empty_list.append(letter)
        print(empty_list)
for i in range(0, len(empty_list)):
    print(empty_list[i] 
"""

"""
new_string: int 
string: str = "hello"
for i in range(0, len(string)):
    if string[i] != "e": 
        new_string = string[i]
print(new_string)
"""
new_word : str = ""
e_list: list[str] = ["e", "E"]
word: str = "hello"
for letter in word: 
    if letter not in e_list: 
        new_word = new_word + letter 
print(new_word)