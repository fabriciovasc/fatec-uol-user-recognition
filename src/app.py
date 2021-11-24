from flask import Flask, Blueprint, request
from flask_cors import CORS

from src.models.classifiers.filter_duplicates import FilterDuplicate

app = Flask(__name__)

bp = Blueprint('main', __name__, url_prefix="/service")
CORS(bp)


@bp.get('/')
def root():
    return 'Use /service/duplicates for get user duplicates'


@bp.get('/duplicates/<int:user_id>')
def get_user_by_id(user_id):
    max_search = request.args.get('max_search') or 10
    print(max_search)
    return FilterDuplicate(user_id, max_search).result


def create_app():
    app.register_blueprint(bp)
    return app
