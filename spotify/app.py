from flask import Flask, render_template, request
from .models import DB
from os import getenv
import pandas as pd
from sqlalchemy import create_engine


def create_app():

    app = Flask(__name__)

    # Config Vars
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route("/")
    def home():
        return render_template('base.html', message='Spotify Recommender')

    @app.route('/reset')
    def reset():
        # drop tables
        DB.drop_all()
        # create tables according to schema in models.py
        DB.create_all()
        # TODO: insert songs into DB
        return render_template('base.html', message = 'DB reset')

    @app.route('/recommend', methods=['POST'])
    def recommend():
        song_title = request.values['song_title']
        print(song_title)

        # Fake Recommended Song Data
        # TODO: Replace this with song recommendations from the ML model
        fake_recommendations = [['Ma Mélodie', 'Feet Peals'],
                                ['Minha Bênção (Ao Vivo)', 'Padre Marcelo Rossi'],
                                ['Stuck In A Glass Elevator', 'The Myriad'],
                                ['Club Hip Hop Beat 2', 'Jorge Quintero'],
                                ['Like...monk-like', 'The Reese Project']]

        return render_template('base.html',
                               message='Spotify Recommender',
                               songs=fake_recommendations)
    
    @app.route('/populate')
    def populate():
        """Function to populate database with entire CSV file"""
        sql_engine = create_engine('sqlite:///test.db', echo=False)
        df = pd.read_csv('/Users/willisbridges/Documents/GitHub/spotify_proj/spotify-12m-songs/tracks_features.csv')
        df.to_sql('Song', sql_engine, index=False, if_exists='append')

        return render_template('base.html', message='Databse loaded')

    return app
