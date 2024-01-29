import csv
from flask import Flask, render_template, request
from .models import Song, db
from os import getenv


def create_app():

    app = Flask(__name__)

    # Config Vars
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route("/")
    def home():
        return render_template('base.html', message='Spotify Recommender')

    @app.route("/reset")
    def reset():
        # drop tables (if they exist)
        db.drop_all()

        # create tables according to the schema in models.py
        db.create_all()

        # TODO: insert data into the DB if needed
        csv_file_path = 'test2.csv'
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data = Song(
                    id=row['id'],
                    name=row['name'],
                    album=row['album'],
                    album_id=row['album_id'],
                    artists=row['artists'],
                    artist_ids=row['artist_ids'],
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
                db.session.add(data)

            db.session.commit()
            print("DB reset")

        return render_template('base.html', message='DB reset')

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
