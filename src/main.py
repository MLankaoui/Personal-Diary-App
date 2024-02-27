import diary_entries, search_entries


file = ""
path = ""


def main():
    

    print("============================")

    name = input("please enter your name : ")

    greetings(name)

    options(name)

def greetings(name):
    print(f"hello mr {name} and welcome!")


def options(name):
    print(f"okey then mr {name} please choose between these options")

    print("""
1) writing a new diary.
2) reviewing a diary
3) editing a diary""")
    option = int(input("> your option here : "))
    if option == 1:
        diary_entries.new_diary()


    elif option == 2:
        search_entries.review_diary(file, path)

    elif option == 3:
        diary_entries.edit_diary()

main()