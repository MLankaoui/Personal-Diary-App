import diary_entries, search_entries

def main():
    print("welcome to the personal diary app")

    print("============================")

    name = input("please enter your name : ")

    greetings(name)

    options(name)

    user_option = options(name)

    if (user_option == 1):
        pass #just for now
    elif (user_option == 2):
        pass

    elif (user_option == 3):
        pass

    elif (user_option == 4):
        pass

    else:
        print('not a valid option')
def greetings(name):
    print(f"hello mr {name} and welcome!")


def options(name):
    print(f"okey then mr {name} please choose between these options")

    print("""
1) writing a new diary.
2) deleting a diary
3) reviewing a diary
4) editing a diaryss""")
    option = int(input("> your option here : "))
    return (option)

main()