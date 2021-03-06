# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())

#TODO 1. Create a dictionary in this format:
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter word: ").upper()
output_list = [phonetic_dictionary[letter] for letter in word]
print(output_list)