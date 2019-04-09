from data import queries


def check_data():
    try:
        actors = queries.get_actors_and_shows()
        return actors
    except Exception as error:
        raise error
