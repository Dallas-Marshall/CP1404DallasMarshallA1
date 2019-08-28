"""
Replace the contents of this module docstring with your own details
Name: Dallas Marshall
Date started: 26/08/19
GitHub URL: https://github.com/cp1404-students/2019-2-a1-Dallas-Marshall
"""

# import file
in_file = open('movies.csv', 'r')
for i, movie in enumerate(in_file):
    line = in_file.readlines()
MOVIES_LOADED = len(line)
VALID_MENU_OPTIONS = "QAWL"
MENU = """Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit""".format(
    MOVIES_LOADED)


def main():
    """program is a list of movies that allows a user to track movies that they have watched and wish to watch."""
    print("Movies To Watch 1.0 - by Dallas Marshall")
    print("{} movies loaded".format(MOVIES_LOADED))
    menu_selection = get_user_input()
    while menu_selection != 'Q':
        if menu_selection == 'L':
            print("Need to write code for displaying movies")
        elif menu_selection == "A":
            print("Need to write code for adding movies")
        else:
            print("Need to write code for watching movies")
        menu_selection = get_user_input()

def get_user_input():
    print(MENU)
    is_valid_user_input = False
    user_input = input(">>> ").upper()
    while not is_valid_user_input:
        if user_input in VALID_MENU_OPTIONS:
            return user_input
        else:
            print("Invalid Menu Option")
            user_input = input(">>> ").upper()


if __name__ == '__main__':
    main()
