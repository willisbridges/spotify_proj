import csv
from flask import Flask, render_template, request
from models import DB
from models import Song
from os import getenv


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
        csv_file_path = '../tracks_features.csv'
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data = Song(
                    csv_id=row['csv_id'],
                    name=row['name'],
                    album=row['album'],
                    album_id=row['album_id'],
                    artists=row['artists'],
                    artist_id=row['artist_id'],
                    track_number=row['track_number'],
                    disc_number=row['disc_number'],
                    explicit=row['explicit'],
                    danceability=row['danceability'],
                    energy=row['energy'],
                    key=row['key'],
                    loudness=row['loudness'],
                    mode=row['mode'],
                    speechiness=row['speechiness'],
                    acousticness=row['acousticness'],
                    instrumentalness=row['instrumentalness'],
                    liveness=row['liveness'],
                    valence=row['valence'],
                    tempo=row['tempo'],
                    duration_ms=row['duration_ms'],
                    time_signature=row['time_signature'],
                    year=row['year'],
                    release_date=row['release_date']
                )
                DB.session.add(data)

            DB.session.commit()

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
    return app
