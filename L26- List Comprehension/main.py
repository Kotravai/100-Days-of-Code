import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass



student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# df = pandas.read_csv("nato_phonetic_alphabet.csv")
# #phonetics_dict = df.set_index('letter').to_dict()['code']
# pho_dict = {row.letter:row.code for (index,row) in df.iterrows()}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
# word = input("Enter a word: ").upper()
# final = {l: pho_dict[l] for l in word}
# print(list(final.values()))

# Exception Handling for NATO Phonetic Alphabet - L30 - Errors exceptions

df = pandas.read_csv("nato_phonetic_alphabet.csv")
#phonetics_dict = df.set_index('letter').to_dict()['code']
pho_dict = {row.letter:row.code for (index,row) in df.iterrows()}

loop = True

def generate_phonetic():

    word = input("Enter a word: ").upper()
    try:
        final = [pho_dict[l] for l in word]
    except KeyError:
        print("Kindly enter alphabet only")
        generate_phonetic()
    else:
        print(final)

generate_phonetic()