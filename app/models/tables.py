from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    senha = db.Column(db.String(30), nullable=False)

    def __init__(self, nome, username, senha) -> None:
        self.nome = nome
        self.username = username
        self.senha = senha

    @staticmethod
    def create(nome, username, senha):
        new_user = Users(nome, username, senha)
        db.session.add(new_user)
        db.session.commit()
    
    def __repr__(self):
        return f'User %r>' % self.nome


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    overview = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(100), nullable=False)
    vote_average = db.Column(db.Float, nullable=False)
    vote_count = db.Column(db.Integer, nullable=False)

    def __init__(self, id, title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count
    
    @staticmethod
    def add_movie(id, title, overview, poster, vote_average, vote_count):
        if Movies.query.filter_by(id=id).first():
            pass
        else:
            new_movie = Movies(id, title, overview, poster, vote_average, vote_count)
            db.session.add(new_movie)
            db.session.commit()
    
    def __repr__(self):
        return f'Movie %r>' % self.title