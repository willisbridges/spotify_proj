from flask_sqlalchemy import SQLAlchemy

# creating the database and connecting to it.
db = SQLAlchemy()


# Creating the sqlalchemyclass based on columns in CSV
class Song(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    album = db.Column(db.String(255))
    album_id = db.Column(db.String(255))
    artists = db.Column(db.String(255))
    artist_ids = db.Column(db.String(255))
    track_number = db.Column(db.Integer)
    disc_number = db.Column(db.Integer)
    explicit = db.Column(db.String(255))
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    key = db.Column(db.Integer)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    speechiness = db.Column(db.Float)
    acousticness = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    liveness = db.Column(db.Float)
    valence = db.Column(db.Float)
    tempo = db.Column(db.Float)
    duration_ms = db.Column(db.Integer)
    time_signature = db.Column(db.Integer)
    year = db.Column(db.Integer)
    release_date = db.Column(db.String(255))