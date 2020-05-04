from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

APP = Flask(__name__)


@APP.route('/')
def index():
    return render_template('index.html')



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