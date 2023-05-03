'''Implements functions for making predictions.'''
import random

MOVIES = [
    'Avatar',
    'The Great Beauty',
    'Star Wars',
    'Interstelar',
]

def random_recommender():
    random.shuffle(MOVIES)
    top_two = MOVIES[0:2]
    return top_two

# def random_recommender():
#     random.shuffle(MOVIES)
#     top_two = MOVIES[0:2]
#     return str(top_two)

