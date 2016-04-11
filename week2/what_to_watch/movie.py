import csv

class Movie:
    def __init__(self, movie_id, title):
        self.movie_id = movie_id
        self.title = title
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def read_movies(file_name):
        movies = {}

        with open(file_name, 'r', encoding='latin_1') as movies_file:
            reader = csv.DictReader(movies_file, fieldnames=['movie_id', 'title'], delimiter='|')
            for row in reader:
                movie_id = row['movie_id']
                movies[movie_id] = Movie(movie_id, row['title'])

        return movies
