"""
Replace the contents of this module docstring with your own details
Name: Dallas Marshall
Date started: 26/08/19
GitHub URL: https://github.com/cp1404-students/2019-2-a1-Dallas-Marshall
"""
import operator

INDEX_OF_TITLE = 0
INDEX_OF_YEAR = 1
INDEX_OF_CATEGORY = 2
INDEX_OF_STATUS = 3


def main():
    """program is a list of movies that allows a user to track movies that they have watched and wish to watch."""
    print("Movies To Watch 1.0 - by Dallas Marshall")
    movies = read_file()
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
            print("Invalid menu choice")
        print(menu)
        menu_selection = input(">>> ").upper()
    print("{} movies saved to movies.csv\nHave a nice day :)".format(len(movies)))
    save_movies(movies)


def read_file():
    """Reads the file containing movies saving as a list."""
    movies = []
    in_file = open('movies.csv', 'r')
    for line in in_file:
        line_str = line.strip().split(',')
        movie = [line_str[INDEX_OF_TITLE], int(line_str[INDEX_OF_YEAR]), line_str[INDEX_OF_CATEGORY],
                 line_str[INDEX_OF_STATUS]]
        movies.append(movie)
    in_file.close()
    return movies


def add_movie(movies):
    """Adds new movie to list."""
    new_title = get_valid_selection("Title")
    new_year = get_valid_year()
    new_category = get_valid_selection("Category")
    movies.append([new_title, new_year, new_category, 'u'])
    print("{} ({} from {}) added to movie list".format(new_title, new_category, new_year))


def list_movies(movies):
    """Sorts movies by year and prints formatted table labeling unwatched with *."""
    movies.sort(key=operator.itemgetter(int(1)))
    for i in range(len(movies)):
        unwatched_string = ' '
        if not is_movie_watched(movies, i):
            unwatched_string = '*'
        print(" {}. {} {:{}} - {:5} ({})".format(i, unwatched_string, movies[i][INDEX_OF_TITLE], longest_title(movies),
                                                 movies[i][INDEX_OF_YEAR], movies[i][INDEX_OF_CATEGORY]))
    print("{} movies watched, {} movies still to watch".format(number_movies_status(movies, 'w'),
                                                               number_movies_status(movies, 'u')))


def number_movies_status(movies, status):
    """Returns count of status e.g. (watched (w) or unwatched(u)."""
    movie_count = 0
    for i in range(len(movies)):
        if movies[i][INDEX_OF_STATUS] == '{}'.format(status):
            movie_count += 1
    return movie_count


def is_movie_watched(movies, i):
    """Returns True if movie is watched, else returns False."""
    if movies[i][INDEX_OF_STATUS].lower() == 'w':
        return True
    else:
        return False


def watch_movie(movies):
    """Sets a chosen movie as watched."""
    if number_movies_status(movies, 'u') == 0:
        return print("No more movies to watch!")

    print("Enter the number of a movie to mark as watched")
    movie_index = get_valid_input(movies)

    if is_movie_watched(movies, movie_index):
        print("You have already watched {}".format(movies[movie_index][INDEX_OF_TITLE]))
    else:
        movies[movie_index][INDEX_OF_STATUS] = 'w'
        print("{} from {} watched".format(movies[movie_index][INDEX_OF_TITLE], movies[movie_index][INDEX_OF_YEAR]))


def get_valid_input(movies):
    """Returns valid movie index input. """
    is_valid_input = False
    while not is_valid_input:
        try:
            movie_index = int(input(">>> "))
            if movie_index < 0:
                print("Number must be >= 0")
            elif movie_index > (len(movies) - 1):
                print("Invalid movie number")
            else:
                is_valid_input = True
                return movie_index
        except ValueError:
            print("Invalid input; enter a valid number")


def longest_title(movies):
    """Returns longest movie title length."""
    longest_title_length = 0
    for movie in movies:
        title_length = len(movie[INDEX_OF_TITLE])
        if title_length > longest_title_length:
            longest_title_length = title_length
    return longest_title_length


def get_valid_selection(prompt):
    """Returns a valid (prompt).

     Keyword arguments:
     prompt -- the string displayed to the user
     """
    user_input = input("{}: ".format(prompt))
    while not user_input.strip():
        print("Input can not be blank")
        user_input = input("{}: ".format(prompt))
    return user_input


def get_valid_year():
    """Returns a valid year input."""
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


def save_movies(movies):
    out_file = open('movies.csv', 'w')
    movies.sort(key=operator.itemgetter(int(1)))
    for movie in movies:
        line = list_to_string(movie)
        out_file.write("{}\n".format(line))
    out_file.close()


def list_to_string(list_of_data):
    """Return a list as a string."""
    string = ""
    for element in list_of_data:
        string += str("{},".format(element))
    return string


if __name__ == '__main__':
    main()
