#file detection

import os

"""# a file/directory in a variable
file_path = "/home/kali/Desktop/test" 

#importing os func to file.fir
if os.path.exists(file_path):
    print(f"The location {file_path} exists")

    # check if it is a file
    if os.path.isfile(file_path):
        print("that is a file")
        # check if it is a directory
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location does not exist")"""


# Pytho nwriting files (.txt, .json, .csv)

# txt_data = "Take out the president,\n Take out the other presidents,\n Take out bandits"

# Create a list of three things you want to do 

ideas = ["Blow up the house of assembly", "Steal all the money I can", "Imprison Desmod Elliot"]

file = open("ideas.txt", "r", encoding="utf-8") as f:
for idea in ideas:
    file.write(f"{idea}\n")







