
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read().split("\n")
    
with open("./Input/Letters/starting_letter.txt") as letter:
    text = letter.read()
    for name in names:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
            new_letter.write(text.replace("[name]", name))