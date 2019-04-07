from data import queries


def check_shows():
    try:
        shows = queries.get_shows_for_table()
        return shows
    except Exception as err:
        return err


