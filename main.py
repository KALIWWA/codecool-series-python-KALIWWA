from flask import Flask, render_template, jsonify
from data import queries
from data_manager import shows, seasons

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/tv-show/<show_id>')
def show_details(show_id):
    show = queries.get_show_details(show_id)
    return render_template('show_details.html', show=show)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/table', methods=['GET', 'POST'])
def json_table():
    shows_table = shows.check_shows()
    return jsonify(shows_table)


@app.route('/tv-show/<show_id>/<season_id>')
def show_season_details(show_id, season_id):
    pass


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
