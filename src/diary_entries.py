import os
from datetime import datetime

def new_diary(filename, path, content):
    print("please enter a file name were you want everything to be inserted : ")
    filename = input("> your file name here : ")


    content = input("please put here your content : ")
    path = input("enter the directory where you want to put your want to save the file")

    if not os.path.exists(path):
        print("directory doesn't exist")
        return
    
    time_now = datetime.now()

    timestamp = time_now.strftime("%Y-%m-%d_%H-%M-%S")

    with open(f"{path}/{timestamp}.txt", "w") as filename:
        filename.write(content)