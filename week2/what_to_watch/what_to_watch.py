import csv
from movie import Movie
from user import User

movies = Movie.read_movies('u.item')

users = User.read_users('u.user')

class Rating:
    def __init__(self, user_id, movie_id, score):
        self.user_id = user_id
        self.movie_id = movie_id
        self.score = score

def add_rating(rating):
    movie = movies[movie_id]
    movie.add_rating(rating)

    user = users[user_id]
    user.add_rating(rating)

with open('u.data', 'r') as movies_file:
    reader = csv.DictReader(movies_file, fieldnames=['user_id', 'movie_id', 'score'], delimiter='\t')
    for row in reader:
        user_id = row['user_id']
        movie_id = row['movie_id']
        score = row['score']

        rating = Rating(user_id, movie_id, score)

        add_rating(rating)

print(len(users['456'].ratings))

print([rating.user_id for rating in users['123'].ratings])
