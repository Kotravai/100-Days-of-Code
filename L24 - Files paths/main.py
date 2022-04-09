# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


replacement_text = "[name]"
with open("../L24 - Mail Merge/Input/Letters/starting_letter.txt", "r+") as start:
    letter = start.readlines()
    with open("../L24 - Mail Merge/Input/Names/invited_names.txt") as names:
        while True:
            next_name = names.readline()
            next_name.strip()
            for string in letter:
                if replacement_text in string:
                    new_string = string.replace(replacement_text, str(next_name))
                else:
                    new_string = string
                with open(f"../L24 - Mail Merge/Output/ReadyToSend/letter to {next_name}.txt", "a") as final_one:
                    final_one.write(new_string)
            if not next_name:
                break
            print(next_name.strip())