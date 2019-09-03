"""
Replace the contents of this module docstring with your own details
Name: Dallas Marshall
Date started: 26/08/19
GitHub URL: https://github.com/cp1404-students/2019-2-a1-Dallas-Marshall
"""
import operator


def main():
    """program is a list of movies that allows a user to track movies that they have watched and wish to watch."""
    movies = []
    in_file = open('movies.csv', 'r')
    for line_str in in_file:
        line_list = line_str.strip().split(',')
        line_list[1] = int(line_list[1])  # Convert year into integer
        movies.append(line_list)
    in_file.close()

    print("Movies To Watch 1.0 - by Dallas Marshall")
    menu = """Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit"""
    print("{} movies loaded\n{}".format(len(movies), menu))

    menu_selection = input(">>> ").upper()
    while menu_selection != 'Q':
        if menu_selection == 'L':
            list_movies(movies)
        elif menu_selection == 'A':
            add_movie(movies)
        elif menu_selection == 'W':
            print("WATCHING MOVIES...")
        else:
            print("Invalid Menu Option")
        print("""Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit""")
        menu_selection = input(">>> ").upper()
    print("ADD ending msg and saving code")


def add_movie(movies):
    new_title = get_valid("Title")
    new_year = get_valid_year()
    new_category = get_valid("Category")
    movies.append([new_title, new_year, new_category, 'u'])
    print("{} ({} from {}) added to movie list".format(new_title, new_category, new_year))


def list_movies(movies):
    """Program takes list of movies, sorts them by year published and then prints formatted table labeling unwatched"""
    movies_unwatched = 0
    movies_watched = 0
    longest_title_length = get_longest_title(movies)
    # Convert all years to integers and then sort list by years
    for i in range(len(movies)):
        movies[i][1] = int(movies[i][1])
    movies.sort(key=operator.itemgetter(int(1)))
    # List movies in formatted table with unwatched movies marked with an *
    for i in range(len(movies)):
        if movies[i][3].lower() == 'u':
            movies_unwatched += 1
            print("{}. * {:{}} - {:5} ({})".format(i, movies[i][0], longest_title_length,
                                                   movies[i][1], movies[i][2]))
        else:
            print("{}.   {:{}} - {:5} ({})".format(i, movies[i][0], longest_title_length,
                                                   movies[i][1], movies[i][2]))
            movies_watched += 1
    print("{} movies watched, {} movies still to watch".format(movies_watched, movies_unwatched))


def get_longest_title(movies):
    """Program calculates the longest movie name and returns length as an integer."""
    longest_title_length = 0
    for movie in movies:
        title_length = len(movie[0])
        if title_length > longest_title_length:
            longest_title_length = title_length
    return longest_title_length


# Get a valid input for a certain for
def get_valid(selection):
    """Program takes a string, then asks the user for (string): and checks a valid response is entered. """
    user_input = input("{}: ".format(selection))
    while not user_input.strip():
        print("Input can not be blank")
        user_input = input("{}: ".format(selection))
    return user_input.title()


def get_valid_year():
    is_valid_year = False
    while not is_valid_year:
        try:
            new_year = int(input("Year: "))
            if new_year < 0:
                print("Number must be >= 0")
            else:
                is_valid_year = True
                return new_year
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()
