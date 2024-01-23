from flask_sqlalchemy import SQLAlchemy

# creating the database and connecting to it.
DB = SQLAlchemy()


# Creating the sqlalchemyclass based on columns in CSV
class Song(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    csv_id = DB.Column(DB.String(255), unique=True)
    name = DB.Column(DB.String(255))
    album = DB.Column(DB.String(255))
    album_id = DB.Column(DB.String(255))
    artists = DB.Column(DB.String(255))
    artist_id = DB.Column(DB.String(255))
    track_number = DB.Column(DB.Integer)
    disc_number = DB.Column(DB.Integer)
    explicit = DB.Column(DB.String(255))
    danceability = DB.Column(DB.Float)
    energy = DB.Column(DB.Float)
    key = DB.Column(DB.Integer)
    loudness = DB.Column(DB.Float)
    mode = DB.Column(DB.Integer)
    speechiness = DB.Column(DB.Float)
    acousticness = DB.Column(DB.Float)
    instrumentalness = DB.Column(DB.Float)
    liveness = DB.Column(DB.Float)
    valence = DB.Column(DB.Float)
    tempo = DB.Column(DB.Float)
    duration_ms = DB.Column(DB.Integer)
    time_signature = DB.Column(DB.Integer)
    year = DB.Column(DB.Integer)
    release_date = DB.Column(DB.Date)
