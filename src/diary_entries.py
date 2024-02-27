import os
from datetime import datetime

def new_diary(filename, path):
    filename = input("Please enter a file name where you want everything to be inserted: ")

    print("Please put your content!")

    lines = []

    while True:
        user_input = input()

        # If user pressed Enter without a value, break out of loop
        if user_input == '':
            break
        else:
            lines.append(user_input + '\n')

    path = input("Enter the directory where you want to save the file: ")

    if not os.path.exists(path):
        print("Directory doesn't exist. Creating directory.")
        os.makedirs(path)

    time_now = datetime.now()

    timestamp = time_now.strftime("%Y-%m-%d_%H-%M-%S")

    with open(f"{path}/{filename}_{timestamp}.txt", "w") as file:
        file.write(''.join(lines))
