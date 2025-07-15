from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cast(db.Model):
    __tablename__ = 'cast'

    cast_id = db.Column(db.INT, primary_key=True)
    cast_full_name = db.Column(db.String(50), nullable=True)
    cast_first_name = db.Column(db.String(50), nullable=True)
    cast_last_name = db.Column(db.String(50), nullable=True)
    cast_gender = db.Column(db.String(2), nullable=True)

    def asdict(self):
        return {
            'cast_id': self.cast_id,
            'cast_full_name': self.cast_full_name,
            'cast_first_name': self.cast_first_name,
            'cast_last_name': self.cast_last_name,
            'cast_gender': self.cast_gender,
        }

class Cast_Member(db.Model):
    __tablename__ = 'cast_member'

    movie_id = db.Column(db.INT, db.ForeignKey('movie.movie_id'), primary_key=True)
    cast_id = db.Column(db.INT, db.ForeignKey('cast.cast_id'), primary_key=True)

    def asdict(self):
        return {
            'movie_id': self.movie_id,
            'cast_id': self.cast_id,
        }

class Directors(db.Model): 
    __tablename__ = 'director'

    director_id = db.Column(db.INT, primary_key=True, autoincrement=True)
    director_full_name = db.Column(db.String(50), nullable=True)
    director_first_name = db.Column(db.String(50), nullable=True)
    director_last_name = db.Column(db.String(50), nullable=True)
    director_gender = db.Column(db.String(2), nullable=True)

    def asdict(self):
        return {
            'director_id': self.director_id,
            'director_full_name': self.director_full_name,
            'director_first_name': self.director_first_name,
            'director_last_name': self.director_last_name,
            'director_gender': self.director_gender,
        }

class Genre(db.Model):
    __tablename__ = 'genre'

    genre_id = db.Column(db.INT, primary_key=True)
    genre_description = db.Column(db.String(50), nullable=True)

    def asdict(self):
        return {
            'genre_id': self.genre_id,
            'genre_description': self.genre_description,
        }

class Movie(db.Model):
    __tablename__ = 'movie'

    movie_id = db.Column(db.INT, primary_key=True)
    movie_title = db.Column(db.String(150), nullable=True)
    movie_description = db.Column(db.String(250), nullable=True)
    movie_release_date = db.Column(db.DATE, nullable=True)
    movie_duration = db.Column(db.INT, nullable=True)
    director_id = db.Column(db.INT, db.ForeignKey('director.director_id'), nullable=True) 

    director = db.relationship('Directors', backref=db.backref('movies', lazy=True))

    def asdict(self):
        return {
            'movie_id': self.movie_id,
            'movie_title': self.movie_title,
            'movie_description': self.movie_description,
            'movie_release_date': self.movie_release_date.isoformat() if self.movie_release_date else None,
            'movie_duration': self.movie_duration,
            'director_id': self.director_id,
        }

class Movie_Genre(db.Model):
    __tablename__ = 'movie_genre'

    movie_id = db.Column(db.INT, db.ForeignKey('movie.movie_id'), primary_key=True)
    genre_id = db.Column(db.INT, db.ForeignKey('genre.genre_id'), primary_key=True) 

    movie = db.relationship('Movie', backref=db.backref('movie_genres', lazy=True))
    genre = db.relationship('Genre', backref=db.backref('movie_genres', lazy=True))

    def asdict(self):
        return {
            'movie_id': self.movie_id,
            'genre_id': self.genre_id,
        }
