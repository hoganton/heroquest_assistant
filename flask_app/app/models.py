from datetime import datetime
from hashlib import md5
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    heroes = db.relationship('Hero', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    character = db.Column(db.String(140))
    attack_dice = db.Column(db.Integer)
    defend_dice = db.Column(db.Integer)
    starting_body_points = db.Column(db.Integer)
    starting_mind_points = db.Column(db.Integer)
    weapons = db.Column(db.String(140))
    armor = db.Column(db.String(140))
    body_points = db.Column(db.Integer)
    quests = db.Column(db.Integer)
    gold_coins = db.Column(db.Integer)
    items = db.Column(db.String(560))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'character': self.character
        }

    def __repr__(self):
        return '<Hero {}>'.format(self.body)
