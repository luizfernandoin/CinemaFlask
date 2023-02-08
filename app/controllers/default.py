from app import app, db
from ..request import search_movie
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from ..models.tables import Users, Movies
import os
import time

@app.route('/')
def index():
    lista = Movies.query.order_by(Movies.id)
    return render_template('lista.html', titulo='', movies=lista)

@app.route('/cadastro')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('cadastro')))
    return render_template('cadastro.html', titulo='Novo Filme')

@app.route('/criar', methods=['POST',])
def criar():
    title = request.form['nome']
    overview = request.form['overview']
    avaliacao = request.form['avaliacao']
    tot_avaliacao = request.form['tot_avaliacao']

    movie = Movies.query.filter_by(title=title).first()

    if movie:
        flash('Filme já existente!')
        return redirect(url_for('index'))

    novo_movie = Movies(id=None, title=title,overview=overview,poster='False',vote_average=avaliacao,vote_count=tot_avaliacao)

    db.session.add(novo_movie)
    db.session.commit()

    capa = request.files['capa']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    capa.save(f'{upload_path}/capa{novo_movie.id}-{timestamp}.jpg')


    flash('Filme criado com sucesso!')
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    movie = Movies.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editar Movie', movie=movie)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    movie = Movies.query.filter_by(id=request.form['id']).first()
    movie.title = request.form['title']
    movie.overview = request.form['overview']
    movie.vote_average = request.form['vote_average']
    movie.vote_count = request.form['vote_count']

    db.session.add(movie)
    db.session.commit()

    flash('Livro atualizado com sucesso!')
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Movies.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Filme deletado com sucesso!')

    return redirect(url_for('index'))

@app.route('/visualizar/<int:id>')
def visualizar(id):
    movie = Movies.query.filter_by(id=id).first()
    capa_movie = recupera_imagem(id)
    return render_template('livro.html', movie=movie, capa=capa_movie)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima, titulo='Login')

@app.route('/signup')
def signup():
    proxima = request.args.get('proxima')
    return render_template('signup.html', proxima=proxima, titulo='Cadastre-se')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Users.query.filter_by(username=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.username
            flash(usuario.username + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuário não logado com sucesso!')
            return redirect(url_for('login'))
    else:
        flash('Usuário não logado com sucesso!')
        return redirect(url_for('login'))

@app.route('/cadastrar_user', methods=['POST',])
def cadastrar_user():
    nome = request.form['nome']
    username = request.form['usuario']
    senha = request.form['senha']
    usuario = Users.query.filter_by(username=request.form['usuario']).first()

    if usuario:
        flash('Usuario já esta em uso!')
        return redirect(url_for('signup'))
    else:
        Users.create(nome, username, senha)
        flash('Usuário cadastrado com sucesso!')
        session['usuario_logado'] = username
        flash(username + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory(app.config['UPLOAD_PATH'], nome_arquivo)

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'livro.png'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'livro.png':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))

@app.route('/visualiza/<int:id>')
def visualiza_imagem(id):
    capa = recupera_imagem(id)
    return imagem(capa)

@app.route('/search', methods=['POST'])
def search():
    movie_name = request.form['search-input']
    
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    print(searched_movies)
    title = f'Resultados para {movie_name}'
    if searched_movies:
        return render_template('search.html', title = title, movies = searched_movies)
    else:
        flash('Não obtivemos respostas válidas!')
        return redirect(url_for('index'))

@app.route('/team')
def team():
    return render_template('team.html')

