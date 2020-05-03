from flask import Flask


APP = Flask(__name__)


@APP.route('/')
def index():
    pass


@APP.route('/games')
def games():
    pass


@APP.route('/games/<game_id>/tables')
def tables(game_id):
    pass


@APP.route('/games/<game_id>/tables/<table_id>')
def table_actions(game_id, table_id):
    pass


@APP.route('/games/<game_id>/tables/<table_id>/update')
def update(game_id, table_id):
    pass