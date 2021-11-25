from flask import Flask, Blueprint, request
from flask_cors import CORS
from flask.json import jsonify

from src.models.classifiers.filter_duplicates import FilterDuplicate

app = Flask(__name__)

bp = Blueprint('main', __name__, url_prefix="/service")
CORS(bp)


@bp.get('/')
def root():
    return 'Use /service/duplicates for get user duplicates'


@bp.get('/duplicates/<int:user_id>')
def get_user_by_id(user_id):
    try:
        return FilterDuplicate(user_id).result
    except Error:
        print(Error)
        return jsonify(
            accuracy=0.0,
            user_duplicates=[]
        )


def create_app():
    app.register_blueprint(bp)
    return app
