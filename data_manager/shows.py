from data import queries


def check_shows():
    try:
        shows = queries.get_shows_for_table()
        return shows
    except Exception as error:
        return error


def check_data(show_id):
    try:
        return queries.get_show_details(show_id)
    except Exception as error:
        raise error
