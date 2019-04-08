from data import db_connection


@db_connection.connection_handler
def get_shows(cursor):
    sql_string = """
                SELECT id, title 
                FROM shows;"""
    cursor.execute(sql_string)
    shows = cursor.fetchall()
    return shows
