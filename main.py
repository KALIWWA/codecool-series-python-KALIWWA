from flask import Flask, render_template
from data import queries

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


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
