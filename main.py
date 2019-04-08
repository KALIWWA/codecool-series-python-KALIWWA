from flask import Flask, render_template, url_for
from data import queries
from data_manager import shows, seasons

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/tv-show/<show_id>')
def show_details(show_id):
    show = shows.check_data(show_id)
    return render_template('show_details.html', show=show)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
