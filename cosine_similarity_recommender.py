import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# read dataset
initial = pd.read_csv('user_item.csv', index_col=0).T

user_item = initial.fillna(value=0)

def cos_sim(vector_one, vector_two):
    num = np.dot(vector_one, vector_two)
    den = np.sqrt(np.dot(vector_one, vector_one))*np.sqrt(np.dot(vector_two, vector_two))
    return num/den

def user_user(df):

    user_user_final = list()
    for user in df.columns:

        user_user_prep = list()
        for other_user in df.columns:
            similarity = cos_sim(df[user], df[other_user])
            user_user_prep.append(similarity)
        
        user_user_final.append(user_user_prep)
    
    user_user_matrix = pd.DataFrame(user_user_final, columns=df.columns, index=df.columns)
    return user_user_matrix



new_user = int(input("Input User# between 0 and 609: "))

user_user_matrix = user_user(user_item).round(2)

user_user_matrix_sklearn = pd.DataFrame(cosine_similarity(user_item.T), columns = user_item.columns, index = user_item.columns)

unseen_movies = initial[initial[new_user].isna()].index

top_five_users = user_user_matrix[new_user].sort_values(ascending=False).index[1:6]



for movie in unseen_movies:
    other_users = initial.columns[~initial.loc[movie].isna()]
    other_users = set(other_users)

    num = 0
    den = 0
    for other_user in other_users.intersection(set(top_five_users)):
        rating = user_item[other_user][movie]
        sim = user_user_matrix[new_user][other_user]
        num = num + (rating*sim)
        den = den + sim + 0.0001
    
    ratio = (num/den).round(1)
    print(movie, ratio) 
