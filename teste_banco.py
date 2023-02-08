import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="cinema-flask",
        user='postgres',
        password='armandim')

# Abra um cursor para realizar operações de banco de dados
cur = conn.cursor()

# Execute um comando: isso cria uma nova tabela
# Execute um comando: isso cria uma nova tabela
cur.execute('DROP TABLE IF EXISTS Movies;')
cur.execute('CREATE TABLE Movies (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'overview text NOT NULL,'
                                 'poster varchar (100) NOT NULL,'
                                 'vote_average numeric NOT NULL,'
                                 'vote_count integer NOT NULL);'
                                 )
cur.execute('DROP TABLE IF EXISTS Users;')
cur.execute('CREATE TABLE Users (id serial PRIMARY KEY,'
                                 'nome varchar (150) NOT NULL,'
                                 'username varchar (30) NOT NULL,'
                                 'senha varchar (30) NOT NULL);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO Movies (title,overview,poster,vote_average,vote_count)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('M3GAN',
             'Uma brilhante roboticista de uma empresa de brinquedos usa inteligência artificial para desenvolver M3GAN, uma boneca realista programada para se relacionar emocionalmente com sua sobrinha recém-órfã. Mas quando a programação da boneca funciona muito bem, ela se torna superprotetora de sua nova amiga... com resultados aterrorizantes.',
             'https://image.tmdb.org/t/p/w500/d9nBoowhjiiYc4FBNtQkPY7c11H.jpg',
             7.6,
             1059)
            )


cur.execute('INSERT INTO Movies (title,overview,poster,vote_average,vote_count)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Gato de Botas 2: O Último Pedido',
             'O Gato de Botas descobre que sua paixão pela aventura cobrou seu preço: ele queimou oito de suas nove vidas, deixando-o com apenas uma vida restante. Gato parte em uma jornada épica para encontrar o mítico Último Desejo e restaurar suas nove vidas.',
             'https://image.tmdb.org/t/p/w500/pSr0JjkI9iM1Yxe9cqrS6YBonAA.jpg',
             8.6,
             2983)
            )


cur.execute('INSERT INTO Users (nome, username, senha)'
            'VALUES (%s, %s, %s)',
            ('Luiz Fernando',
             'Luiz',
             'armandim')
            )

conn.commit()

cur.close()
conn.close()