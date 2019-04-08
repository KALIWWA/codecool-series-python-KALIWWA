from data import queries


def check_data(show_id):
    try:
        return queries.get_show_details(show_id)
    except Exception as error:
        raise error
