import os
from datetime import datetime


def new_diary(filename, path):
    filename = input("Please enter a file name where you want everything to be inserted: ")

    print("Please put your content!")

    lines = []
    line_number = 1
    while True:
        user_input = input(f"{line_number}. ")

        # If user pressed Enter without a value, break out of loop
        if user_input == '':
            break
        else:
            lines.append(user_input + '\n')

        line_number += 1

    path = input("Enter the directory where you want to save the file: ")

    if not os.path.exists(path):
        print("Directory doesn't exist. Creating directory.")
        os.makedirs(path)

    with open(f"{path}/{filename}.txt", "w") as file:
        file.write(''.join(lines))



def edit_diary(filename, path):
    path = input("> please enter your file path : ")
    filename = input("> you file name here : ")

    # Open the file in read mode and display its content
    with open(f"{path}/{filename}.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            print(f"{i+1}. {line}")

    # Ask the user which line they want to edit
    line_num = int(input("Enter the line number you want to edit: "))
    new_text = input("Enter the new text: ")

    # Replace the selected line with the new text
    lines[line_num - 1] = new_text

    # Write the modified content back to the file
    with open(f"{path}/{filename}.txt", "w") as file:
        file.writelines(lines)

    print("The file has been updated.")


    


