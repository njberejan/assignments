import csv

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def read_users(file_name):
        users = {}

        with open(file_name, 'r') as users_file:
            reader = csv.DictReader(users_file, fieldnames=['user_id'], delimiter='|')
            for row in reader:
                user_id = row['user_id']
                users[user_id] = User(user_id)

        return users
