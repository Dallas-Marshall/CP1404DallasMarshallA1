"""
Replace the contents of this module docstring with your own details
Name: Dallas Marshall
Date started: 26/08/19
GitHub URL: https://github.com/cp1404-students/2019-2-a1-Dallas-Marshall
"""
import operator

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
            movies_unwatched = 0
            movies_watched = 0
            longest_title_length = get_longest_title()
            movies.sort(key=operator.itemgetter(1))
            # List movies in formatted table with unwatched movies marked with an *
            for movie in range(len(movies)):
                if movies[movie][3].lower() == 'u':
                    movies_unwatched += 1
                    print("{}. * {:{}} - {:5} ({})".format(movie, movies[movie][0], longest_title_length,
                                                           movies[movie][1], movies[movie][2]))
                else:
                    print("{}.   {:{}} - {:5} ({})".format(movie, movies[movie][0], longest_title_length,
                                                           movies[movie][1], movies[movie][2]))
                    movies_watched += 1
            print("{} movies watched, {} movies still to watch".format(movies_watched, movies_unwatched))
        elif menu_selection == "A":
            new_title = get_valid_title()
            new_year = get_valid_year()
            new_category = get_valid_category()
            movies.append([new_title, new_year, new_category, 'u'])
            print("{} ({} from {}) added to movie list".format(new_title, new_category, new_year))
        else:
            print("Need to write code for watching movies")
        menu_selection = get_user_input()
    print("ADD ending msg and saving code")


def get_longest_title():
    longest_title_length = 0
    for movie in movies:
        title_length = len(movie[0])
        if title_length > longest_title_length:
            longest_title_length = title_length
    return longest_title_length


def get_valid_title():
    new_title = input("Title: ")
    while not new_title.strip():
        print("Input can not be blank")
        new_title = input("Title: ")
    return new_title.title()


def get_valid_year():
    is_valid_year = False
    while not is_valid_year:
        try:
            new_year = int(input("Year: "))
            if new_year < 0:
                print("Number must be >= 0")
            else:
                is_valid_year = True
                return str(new_year)
        except ValueError:
            print("Invalid input; enter a valid number")


def get_valid_category():
    new_category = input("Category: ")
    while not new_category.strip():
        print("Input can not be blank")
        new_category = input("Category: ")
    return new_category.title()


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
