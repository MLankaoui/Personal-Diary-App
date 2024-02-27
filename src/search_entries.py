import os
from diary_entries import new_diary

def review_diary(filename, path):
    path = input("> please enter your file path : ")

    filename = input("> you file name here : ")


    with open(f"{path}/{filename}.txt", "r") as filename:
        print(filename.read())