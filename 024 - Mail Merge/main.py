from pathlib import Path

TEMPLATE_FILEPATH = Path("./Input/Letters/starting_letter.txt")
NAMES_FILEPATH = Path("./Input/Names/invited_names.txt")
OUTPUT_FILEPATH = Path("./Output/ReadyToSend")

NAME_PLACEHOLDER = "[name]"

template = ""

with TEMPLATE_FILEPATH.open() as template_file:
    template = "".join(template_file.readlines())

with NAMES_FILEPATH.open() as name_file:
    for name in name_file:
        name = name.replace("\n", "")
        new_letter = template.replace(NAME_PLACEHOLDER, name)
        filename = f"{OUTPUT_FILEPATH}/Letter_to_{name}.txt"
        with open(filename, mode="w") as output_file:
            output_file.write(new_letter)
