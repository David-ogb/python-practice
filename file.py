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

txt_data = "Take out the president,\n Take out the other presidents,\n Take out bandits"

file_path = "/home/kali/Desktop/output.txt"

with open(file=file_path, mode="w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")







