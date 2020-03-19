from flask import render_template, flash, redirect, request
from app import app01, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import flask

@app01.route('/')
@app01.route('/index')
@login_required
def index():
	posts = [
		{
			'autor':	{'username': 'Pepe'},
			'body':		'La gran noticia de Pepe'
		},
		{
			'autor':	{'username': 'Juan'},
			'body':		'La pesima noticia de Juan'
		}
	]
	return render_template('index.html', title='home', posts=posts)

@app01.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(flask.url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Usuario o password invalidos')
			return redirect(flask.url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = flask.url_for('index')
		return redirect(next_page)
	return render_template('login.html', title = 'Sign in', form=form)

@app01.route('/logout')
def logout():
    logout_user()
    return redirect(flask.url_for('index'))

@app01.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(flask.url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		msj = 'Felicidades ' + user.username + ' ya esta registrado!'
		flash(msj)
		return redirect(flask.url_for('login'))
	return render_template('register.html', title='Registro', form=form)