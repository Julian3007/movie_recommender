#import libs
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings(action='ignore')

# Prompt the user for input and store the values in variables


# define movies list
# user_item = pd.read_csv('user_item.csv', index_col='userId')
# MOVIES = list(user_item.columns)


# with open('week_10/10.3_NMF/factorizer_NMF.pkl', 'rb') as file_in:
#     model = pickle.load(file_in)

def recommend_nmf(model, MOVIES, user_query):


    """
    Filters and recommends the top k movies for any given input query based on a trained NMF model. 
    Returns a list of k movie ids.
    """
    # define Q
    Q = model.components_

    recommendations = []

    # 2. construct new_user-item dataframe given the query
    user_input = pd.DataFrame(user_query, index = ['new_user'], columns=MOVIES)

    # using the same imputation as training data
    user_input_imputed = user_input.fillna(value=0)

    # 3. scoring
    P_user = model.transform(user_input_imputed)
    P_user = pd.DataFrame(P_user, index = ['new_user'])

    R_user_hat = np.dot(P_user, Q)
    R_user_hat = pd.DataFrame(R_user_hat, columns=MOVIES, index=['new_user'])

    # 4. ranking
    R_user_hat_transposed = R_user_hat.T.sort_values(by='new_user', ascending=False)
    recommendables = list(R_user_hat_transposed.index)

    # filter out movies already seen by the user
    user_initial_ratings_list = list(user_query.keys())
    user_recommendations = [movie for movie in recommendables if movie not in user_initial_ratings_list]
 
    # return the top-k highest rated movie ids or titles

    recommendations = user_recommendations[:5]
    #print(recommendations)
    return recommendations


