from flask import Blueprint, jsonify
from app.models import Hero

api_bp = Blueprint('api', __name__)

@api_bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.serialize() for hero in heroes])
