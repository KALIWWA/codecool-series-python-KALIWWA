from data import data_manager


@data_manager.connection_handler
def get_shows(cursor):
    sql_string = """
                SELECT id, title 
                FROM shows;"""
    cursor.execute(sql_string)
    shows = cursor.fetchall()
    return shows
