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
    for line in in_file:
        movie = line.strip().split(',')
        movie[1] = int(movie[1])  # Convert year into integer
        movies.append(movie)
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
            watch_movie(movies)
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
    """Function takes list of movies, sorts them by year published and then prints formatted table labeling unwatched"""
    movies_unwatched = 0
    movies_watched = 0
    longest_title_length = get_longest_title(movies)
    # Convert all years to integers and then sort list by years
    for i in range(len(movies)):
        movies[i][1] = int(movies[i][1])
    movies.sort(key=operator.itemgetter(int(1)))
    # List movies in formatted table with unwatched movies marked with an *
    for i in range(len(movies)):
        if not is_movie_watched(movies, i):
            unwatched_icon_parameter = '*'  # If unwatched set variable equal to asterisk
            movies_unwatched += 1
        else:
            unwatched_icon_parameter = ' '  # If watched set variable to equal space (to keep aligned)
            movies_watched += 1
        print("{}. {} {:{}} - {:5} ({})".format(i, unwatched_icon_parameter, movies[i][0], longest_title_length,
                                                movies[i][1], movies[i][2]))
    print("{} movies watched, {} movies still to watch".format(movies_watched, movies_unwatched))


def is_movie_watched(movies, i):
    """Function takes a list of movies and the index of the movie to test
    Returns True if watched, False if Unwatched"""
    if movies[i][3].lower() == 'w':
        return True
    else:
        return False


def watch_movie(movies):
    """Function takes a list of movies and asks the user to specify which movie they would like to set as watched"""
    movies_unwatched = 0
    movies_watched = 0
    for i in range(len(movies)):
        if not is_movie_watched(movies, i):
            movies_unwatched += 1
        else:
            movies_watched += 1
    if movies_unwatched == 0:
        return print("No more movies to watch!")
    print("Enter the number of a movie to mark as watched")
    is_valid_input = False
    while not is_valid_input:
        try:
            movie_index = int(input(">>> "))
            if movie_index < 0:
                print("Number must be >= 0")
            elif movie_index > (len(movies) - 1):
                print("Invalid movie number")
            elif is_movie_watched(movies, movie_index):
                return print("You have already watched {}".format(movies[movie_index][0]))
            else:
                is_valid_input = True
                movies[movie_index][3] = 'w'
                return print("{} from {} watched".format(movies[movie_index][0], movies[movie_index][1]))
        except ValueError:
            print("Invalid input; enter a valid number")


def get_longest_title(movies):
    """Function calculates the longest movie name and returns length as an integer."""
    longest_title_length = 0
    for movie in movies:
        title_length = len(movie[0])
        if title_length > longest_title_length:
            longest_title_length = title_length
    return longest_title_length


def get_valid(selection):
    """Function takes a string, then asks the user for (string): and checks a valid response is entered. """
    user_input = input("{}: ".format(selection))
    while not user_input.strip():
        print("Input can not be blank")
        user_input = input("{}: ".format(selection))
    return user_input.title()


def get_valid_year():
    """Function prompts user input and ensures it is a valid year before returning as an integer"""
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
