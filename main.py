# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.txt") as letter:
    letter_template = letter.readlines()

with open("Input/Names/invited_names.txt") as names:
    for i in names.readlines():
        name = i[:-1]
        new_letter = ""
        for line in letter_template:
            if line == 'Dear [name],\n':
                new_letter += ("Dear " + name + ",\n")
            elif line == '\n':
                new_letter += line
            else:
                new_letter += line
        with open("Output/ReadyToSend/letter_for_" + name + ".txt", mode="w") as out:
            out.write(new_letter)
