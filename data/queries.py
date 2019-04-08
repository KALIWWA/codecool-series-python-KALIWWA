from data import db_connection


@db_connection.connection_handler
def get_shows(cursor):
    sql_string = """
                SELECT id, title 
                FROM shows;"""
    cursor.execute(sql_string)
    shows = cursor.fetchall()
    return shows


@db_connection.connection_handler
def get_show_details(cursor, show_id):
    sql_string = """
                SELECT shows.id, 
                    shows.title, 
                    to_char(shows.year, 'YYYY') as year, 
                    shows.overview, 
                    to_char(shows.runtime, '999') as runtime, 
                    COALESCE(shows.trailer, 'https://www.youtube.com/watch?v=mO-OpFjHRbE') as trailer, 
                    COALESCE(shows.homepage, 'https://hbogo.pl/') as homepage, 
                    shows.rating, 
                    array_agg(DISTINCT seasons.title) as seasons, 
                    array_agg(DISTINCT actors.name) as actors, 
                    array_agg(DISTINCT genres.name) as genres
                FROM shows
                LEFT JOIN show_characters on shows.id = show_characters.show_id
                INNER JOIN actors on show_characters.actor_id = actors.id
                INNER JOIN show_genres on shows.id = show_genres.show_id
                INNER JOIN genres on show_genres.genre_id = genres.id
                INNER JOIN seasons on shows.id = seasons.show_id
                WHERE shows.id = %(id)s
                GROUP BY shows.id;"""
    cursor.execute(sql_string, {'id': show_id})
    show_details = cursor.fetchone()
    return show_details
