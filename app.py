from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_restx import Api, Resource, reqparse, fields
from models import *  

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rith23112004localhost:3306/moviemanagementdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

api = Api(app, version='1.0', title='Movie Management API', description='API for managing movies and related entities.')
api_ns = api.namespace("Movie", path='/moviemanagementdb', description="Databse System and API design.")

#For Get ID
post_id_parser = reqparse.RequestParser()
post_id_parser.add_argument('id', type=int, required=True, help='ID is required')

# Parser for the `Movie` table
post_movie_parser = reqparse.RequestParser()
post_movie_parser.add_argument('movie_id', type=int, required=True, help='Movie ID is required')
post_movie_parser.add_argument('movie_title', type=str, required=True, help='Movie title is required')
post_movie_parser.add_argument('movie_description', type=str, required=True, help='Movie description is required')
post_movie_parser.add_argument('movie_release_date', type=str, required=True, help='Movie release date is required (format: YYYY-MM-DD)')
post_movie_parser.add_argument('movie_duration', type=int, required=True, help='Movie duration (in minutes) is required')
post_movie_parser.add_argument('director_id', type=int, required=True, help='Director ID is required. Make sure that Director ID is exited.')

@api_ns.route('/movie')
class CVUDMovie(Resource):

    #Create
    @api.expect(post_movie_parser)
    def post(self):
        args = post_movie_parser.parse_args()

        try:
            
            t = Movie(movie_id = args["movie_id"], 
                      movie_title = args["movie_title"],
                      movie_description = args["movie_description"],
                      movie_release_date = args["movie_release_date"],
                      movie_duration = args["movie_duration"],
                      director_id = args["director_id"],
                       )

            db.session.add(t)
            db.session.commit()
            return {'message':'success'}, 201

        except Exception as e:
                print (e)
                return {'message': 'Something went wrong!'}, 500
        
    #View
    @api.expect(post_id_parser)
    def get(self):
        args = post_id_parser.parse_args()
        
        movie_id = args["id"]

        movie = db.session.query(Movie).filter(Movie.movie_id == movie_id).first()
        if not movie:
            return {"message": "Movie not found"}, 404
        return movie.asdict(), 200
    
    #Update
    @api.expect(post_movie_parser)
    def put(self):
        args = post_movie_parser.parse_args()

        try:
            movie = db.session.query(Movie).filter(Movie.movie_id == args["movie_id"]).first()

            if not movie:
                return {'message': 'Movie not found'}, 404

            movie.movie_title = args["movie_title"]
            movie.movie_description = args["movie_description"]
            movie.movie_release_date = args["movie_release_date"]
            movie.movie_duration = args["movie_duration"]
            
            db.session.commit()

            return {'message': 'Movie and related data updated successfully'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': f'An error occurred: {str(e)}'}, 500

    #Delete
    @api.expect(post_id_parser)
    def delete(self):
        args = post_id_parser.parse_args()
        movie_id = args["id"]

        movie = db.session.query(Movie).filter(Movie.movie_id == movie_id).first()

        if not movie:
            return {'message': 'There is no record with this ID'}, 400

        cast_members = db.session.query(Cast_Member).filter(Cast_Member.movie_id == movie_id).all()
        director = db.session.query(Directors).filter(Directors.director_id == movie.director_id).first()
        movie_genres = db.session.query(Movie_Genre).filter(Movie_Genre.movie_id == movie_id).all()

        for cast_member in cast_members:
            db.session.delete(cast_member)

        for movie_genre in movie_genres:
            db.session.delete(movie_genre)

        if director:
            if not db.session.query(Movie).filter(Movie.director_id == director.director_id).all():
                db.session.delete(director)

        db.session.delete(movie)

        try:
            db.session.commit()
            return {'message': 'Success'}, 200
        except exc.SQLAlchemyError as e:
            db.session.rollback()  
            return {'message': str(e.__cause__)}, 500

# Director
api_ns2 = api.namespace("Director", path='/moviemanagementdb', description="Table : Directo")
post_director_parser = reqparse.RequestParser()
post_director_parser.add_argument('director_id', type=int, required=True, help='Director ID is required')
post_director_parser.add_argument('director_full_name', type=str, required=True, help='Full name of the director is required')
post_director_parser.add_argument('director_first_name', type=str, required=True, help='First name of the director is required')
post_director_parser.add_argument('director_last_name', type=str, required=True, help='Last name of the director is required')
post_director_parser.add_argument('director_gender', type=str, required=True, help='Gender of the director (M/F) is required')

@api_ns2.route('/director')
class CVUDirector(Resource) :
    
    #Create
    @api.expect(post_director_parser)
    def post(self):
        args = post_director_parser.parse_args()

        try:
            
            t = Directors( director_id = args["director_id"], 
                           director_full_name = args["director_full_name"],
                           director_first_name = args["director_first_name"],
                           director_last_name = args["director_last_name"],
                           director_gender = args["director_gender"]
                    )

            db.session.add(t)
            db.session.commit()
            return {'message':'success'}, 201

        except Exception as e:
                print (e)
                return {'message': 'Something went wrong!'}, 500

    #View
    @api.expect(post_id_parser)
    def get(self):
        args = post_id_parser.parse_args()
        
        director_id = args["id"]

        director = db.session.query(Directors).filter(Directors.director_id == director_id).first()
        if not director:
            return {"message": "Director not found"}, 404
        return director.asdict(), 200

    #Update
    @api.expect(post_director_parser)
    def put(self):

        args = post_director_parser.parse_args()

        try:
            director = db.session.query(Directors).filter(Directors.director_id == args["director_id"]).first()

            if not director:
                return {'message': 'Director not found'}, 404

            director.director_id = args["director_id"]
            director.director_first_name = args["director_first_name"]
            director.director_last_name = args["director_last_name"]
            director.director_full_name = args["director_full_name"]
            director.director_gender = args["director_gender"]
            
            db.session.commit()

            return {'message': 'Director and related data updated successfully'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': f'An error occurred: {str(e)}'}, 500

# Cast
api_ns3 = api.namespace("Cast", path='/moviemanagementdb', description="Table : Cast")
post_cast_parser = reqparse.RequestParser()
post_cast_parser.add_argument('cast_id', type=int, required=True, help='Cast ID is required')
post_cast_parser.add_argument('cast_full_name', type=str, required=True, help='Full name of the cast is required')
post_cast_parser.add_argument('cast_first_name', type=str, required=True, help='First name of the cast is required')
post_cast_parser.add_argument('cast_last_name', type=str, required=True, help='Last name of the cast is required')
post_cast_parser.add_argument('cast_gender', type=str, required=True, help='Gender of the cast (M/F) is required')

@api_ns3.route('/cast')
class CVUCast(Resource) :
    
    #Create
    @api.expect(post_cast_parser)
    def post(self):
        args = post_cast_parser.parse_args()

        try:
            
            t = Cast( cast_id = args["cast_id"], 
                      cast_full_name = args["cast_full_name"],
                      cast_first_name = args["cast_first_name"],
                      cast_last_name = args["cast_last_name"],
                      cast_gender = args["cast_gender"]
                    )

            db.session.add(t)
            db.session.commit()
            return {'message':'success'}, 201

        except Exception as e:
                print (e)
                return {'message': 'Something went wrong!'}, 500

    #View
    @api.expect(post_id_parser)
    def get(self):
        args = post_id_parser.parse_args()
        
        cast_id = args["id"]

        cast = db.session.query(Cast).filter(Cast.cast_id == cast_id).first()
        if not cast:
            return {"message": "Cast not found"}, 404
        return cast.asdict(), 200

    #Update
    @api.expect(post_cast_parser)
    def put(self):

        args = post_cast_parser.parse_args()

        try:
            cast = db.session.query(Cast).filter(Cast.cast_id == args["cast_id"]).first()

            if not cast:
                return {'message': 'Cast not found'}, 404

            cast.cast_id = args["cast_id"]
            cast.cast_first_name = args["cast_first_name"]
            cast.cast_last_name = args["cast_last_name"]
            cast.cast_full_name = args["cast_full_name"]
            cast.cast_gender = args["cast_gender"]
            
            db.session.commit()

            return {'message': 'Cast and related data updated successfully'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': f'An error occurred: {str(e)}'}, 500

# Genre
api_ns4 = api.namespace("Genre", path='/moviemanagementdb', description="Table : Genre")
post_genre_parser = reqparse.RequestParser()
post_genre_parser.add_argument('genre_id', type=int, required=True, help='Genre ID is required')
post_genre_parser.add_argument('genre_description', type=str, required=True, help='Genre description is required')

@api_ns4.route('/genre')
class CVUGenre(Resource) :
    
    #Create
    @api.expect(post_genre_parser)
    def post(self):
        args = post_genre_parser.parse_args()

        try:
            
            t = Genre( genre_id = args["genre_id"], 
                       genre_description = args["genre_description"],
                    )

            db.session.add(t)
            db.session.commit()
            return {'message':'success'}, 201

        except Exception as e:
                print (e)
                return {'message': 'Something went wrong!'}, 500

    #View
    @api.expect(post_id_parser)
    def get(self):
        args = post_id_parser.parse_args()
        
        genre_id = args["id"]

        genre = db.session.query(Genre).filter(Genre.genre_id == genre_id).first()
        if not genre:
            return {"message": "Movie Genre not found"}, 404
        return genre.asdict(), 200

    #Update
    @api.expect(post_genre_parser)
    def put(self):

        args = post_genre_parser.parse_args()

        try:
            genre = db.session.query(Genre).filter(Genre.genre_id == args["genre_id"]).first()

            if not genre:
                return {'message': 'Movie Genre not found'}, 404

            genre.genre_id = args["genre_id"]
            genre.genre_description = args["genre_description"]
            
            db.session.commit()

            return {'message': 'Movie Genre and related data updated successfully'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': f'An error occurred: {str(e)}'}, 500

# Cast Member
api_ns5 = api.namespace("Cast Member", path='/moviemanagementdb', description="Table : Cast Member")
put_cast_member_parser = reqparse.RequestParser()
put_cast_member_parser.add_argument('movie_id', type=int, required=True, help='Movie ID is required')
put_cast_member_parser.add_argument('cast_id', type=int, required=True, help='Cast ID is required')
put_cast_member_parser.add_argument('new_cast_id', type=int, required=True, help='New Cast ID is required')

post_cast_member_parser = reqparse.RequestParser()
post_cast_member_parser.add_argument('movie_id', type=int, required=True, help='Movie ID is required')
post_cast_member_parser.add_argument('cast_id', type=int, required=True, help='Cast ID is required')

@api_ns5.route('/castmember')
class CVUCastMember(Resource) :
    
    # Create
    @api.expect(post_cast_member_parser)
    def post(self):
        args = post_cast_member_parser.parse_args()

        try:
            
            t = Cast_Member(movie_id = args["movie_id"], 
                            cast_id = args["cast_id"],
                       )

            db.session.add(t)
            db.session.commit()
            return {'message':'success'}, 201

        except Exception as e:
                print (e)
                return {'message': 'Something went wrong!'}, 500

    # View
    @api.expect(post_id_parser)
    def get(self):
        args = post_id_parser.parse_args()
        
        movie_id = args["id"]

        cast_members = db.session.query(Cast_Member).filter(Cast_Member.movie_id == movie_id).all()
        
        if not cast_members:
            return {"message": "No cast members found for the given movie ID"}, 404

        result = [cm.asdict() for cm in cast_members]
        return {"cast_members": result}, 200
    
    # Update
    @api.expect(put_cast_member_parser)
    def put(self):
        args = put_cast_member_parser.parse_args()

        try:
            cast_member = db.session.query(Cast_Member).filter(
                Cast_Member.movie_id == args["movie_id"],
                Cast_Member.cast_id == args["cast_id"]
            ).first()

            if not cast_member:
                return {'message': 'Cast Member not found for the given movie ID and cast ID'}, 404

            cast_member.cast_id = args["new_cast_id"]
            db.session.commit()

            return {'message': 'Cast Member updated successfully'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': f'An error occurred: {str(e)}'}, 500

# Movie Genre
api_ns6 = api.namespace("Movie Genre", path='/moviemanagementdb', description="Table : Movie Genre")
post_movie_genre_parser = reqparse.RequestParser()
post_movie_genre_parser.add_argument('movie_id', type=int, required=True, help='Movie ID is required')
post_movie_genre_parser.add_argument('genre_id', type=int, required=True, help='Genre ID is required')

put_movie_genre_parser = reqparse.RequestParser()
put_movie_genre_parser.add_argument('movie_id', type=int, required=True, help='Movie ID is required')
put_movie_genre_parser.add_argument('genre_id', type=int, required=True, help='Genre ID is required')
put_movie_genre_parser.add_argument('new_genre_id', type=int, required=True, help='New Genre ID is required')


@api_ns6.route('/moviegenre')
class CVUMovieGenre(Resource) :
    
    #Create
    @api.expect(post_movie_genre_parser)
    def post(self):
        args = post_movie_genre_parser.parse_args()

        try:
            
            t = Movie_Genre( movie_id = args["movie_id"], 
                             genre_id = args["genre_id"]
                            )

            db.session.add(t)
            db.session.commit()
            return {'message':'success'}, 201

        except Exception as e:
                print (e)
                return {'message': 'Something went wrong!'}, 500

    # View
    @api.expect(post_id_parser)
    def get(self):
        args = post_id_parser.parse_args()
        
        movie_id = args["id"]

        moive_genre = db.session.query(Movie_Genre).filter(Movie_Genre.movie_id == movie_id).all()
        
        if not moive_genre:
            return {"message": "No Movie Genre found for the given movie ID"}, 404

        result = [cm.asdict() for cm in moive_genre]
        return {"moive_genre": result}, 200

    # Update
    @api.expect(put_movie_genre_parser)
    def put(self):
        args = put_movie_genre_parser.parse_args()

        try:
            movie_genre = db.session.query(Movie_Genre).filter(
                Movie_Genre.movie_id == args["movie_id"],
                Movie_Genre.genre_id == args["genre_id"]
            ).first()

            if not movie_genre:
                return {'message': 'Movie Genre not found for the given movie ID and genre ID'}, 404

            movie_genre.genre_id = args["new_genre_id"]
            db.session.commit()

            return {'message': 'Movie Genre updated successfully'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': f'An error occurred: {str(e)}'}, 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
