# Movie Ratings Database

movies = [
    ("Inception", [9, 8, 10, 9]),
    ("Titanic", [8, 9, 7, 8]),
    ("Avengers", [9, 9, 10, 8]),
    ("Joker", [8, 7, 9, 8])
]

def show_movie_ratings():
    print("\nMovie Ratings:")
    for title, ratings in movies:
        avg = sum(ratings) / len(ratings)
        print(f"{title}: {avg:.1f} / 10")

def high_rated_movies():
    print("\nHighly Rated Movies (avg ≥ 9):")
    for title, ratings in movies:
        if sum(ratings) / len(ratings) >= 9:
            print(title)

show_movie_ratings()
high_rated_movies()
