import diary_entries, search_entries


file = ""
path = ""


def main():
    

    print("============================")

    name = input("please enter your name : ")

    greetings(name)

    options(name)

    
    '''elif (user_option == 2):
        pass

    elif (user_option == 3):
        pass

    elif (user_option == 4):
        pass

    else:
        print('not a valid option')'''
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
    if option == 1:
        diary_entries.new_diary(file, path)

    elif option == 3:
        search_entries.review_diary(file, path)

main()