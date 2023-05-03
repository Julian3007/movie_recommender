from flask import Flask, render_template, request
from NMF import recommend_nmf
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings(action='ignore')
with open('factorizer_NMF.pkl', 'rb') as file_in:
    model = pickle.load(file_in)

user_item = pd.read_csv('user_item.csv', index_col='userId')
MOVIES = list(user_item.columns)

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/results')
def recommender():
    user_query = request.args.to_dict()
    user_query = {key:int(value) for key,value in user_query.items()}
    top_5 = recommend_nmf(model, MOVIES, user_query)
    return render_template('results.html', movies = top_5)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
