import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (_, row) in data.iterrows()}

user_prompt = input("Enter a name: ").upper()

result = [alphabet[c] for c in user_prompt]
print(result)
