from data import queries


def check_data(season_id):
    try:
        return queries.get_season_details(season_id)
    except Exception as error:
        raise error
