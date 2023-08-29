from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, HeroForm
from app.models import User, Hero


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/create_hero', methods=['GET', 'POST'])
@login_required
def create_hero():
    form = HeroForm()
    if form.validate_on_submit():
        new_hero = Hero(
            name=form.name.data,
            character=form.character.data,
            attack_dice=form.attack_dice.data,
            defend_dice=form.defend_dice.data,
            starting_body_points=form.starting_body_points.data,
            starting_mind_points=form.starting_mind_points.data,
            weapons=form.weapons.data,
            armor=form.armor.data,
            body_points=form.body_points.data,
            quests=form.quests.data,
            gold_coins=form.gold_coins.data,
            items=form.items.data,
            user_id=current_user.id
        )
        db.session.add(new_hero)
        db.session.commit()
        flash('Hero created successfully!', 'success')
        return redirect(url_for('view_heroes'))
    return render_template('create_hero.html', title='Create Hero', form=form)

@app.route('/view_heroes')
@login_required
def view_heroes():
    user_heroes = Hero.query.filter_by(user_id=current_user.id).all()
    return render_template('view_heroes.html', heroes=user_heroes)

@app.route('/hero_details/<int:hero_id>')
@login_required
def hero_details(hero_id):
    hero = Hero.query.get_or_404(hero_id)
    return render_template('hero_details.html', hero=hero)

@app.route('/delete_hero/<int:hero_id>', methods=['POST'])
def delete_hero(hero_id):
    hero = Hero.query.get_or_404(hero_id)
    db.session.delete(hero)
    db.session.commit()
    flash('Hero deleted successfully.', 'success')
    return redirect(url_for('view_heroes'))

@app.route('/api/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.serialize() for hero in heroes]), 200
