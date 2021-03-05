"""for...in loop exampless"""

#iterate through each item in a list 
letters:list[str] = ["a", "b", "c", "d", "e", "f", "g"]
print("Each letter...")
for letter in letters: 
    print(letter)

#every other number
print("Every other letter...")
for i in range(0, len(letters), 2):
    print(letters[i])

# iterate through each index in a sequence
for i in range(len(letters)):
    print(f"i: {i} - letters[i]: {letters[i]}")