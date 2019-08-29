"""
Replace the contents of this module docstring with your own details
Name: Dallas Marshall
Date started: 26/08/19
GitHub URL: https://github.com/cp1404-students/2019-2-a1-Dallas-Marshall
"""

# import file
in_file = open('movies.csv', 'r')
movies_data = in_file.readlines()
movies = [movie.strip().split(',') for movie in movies_data]
movies_loaded = len(movies)
VALID_MENU_OPTIONS = "QAWL"
MENU = """Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit""".format(
    movies_loaded)


def main():
    """program is a list of movies that allows a user to track movies that they have watched and wish to watch."""
    print("Movies To Watch 1.0 - by Dallas Marshall")
    print("{} movies loaded".format(movies_loaded))
    menu_selection = get_user_input()
    while menu_selection != 'Q':
        if menu_selection == 'L':
            # iterate through movies and if not watched assign asterisk else add space to keep lined up
            for index in range(len(movies)):
                if movies[index][3] == 'u':
                    movies[index][0] = '* ' + movies[index][0]
                else:
                    movies[index][0] = '  ' + movies[index][0]
            # print(movies)
            for i in range(movies_loaded):
                print("{}. {:40} - {:5} ({})".format(i, movies[i][0], movies[i][1], movies[i][2]))
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
