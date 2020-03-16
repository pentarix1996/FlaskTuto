from flask import render_template, flash, redirect
from app import app01
from app.forms import LoginForm
import flask

@app01.route('/')
@app01.route('/index')
def index():
	user = {'username': 'Toni'}
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
	return render_template('index.html', title='home', user=user, posts=posts)

@app01.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
				form.username.data, form.remember_me.data))
		return redirect(flask.url_for('index'))
	return render_template('login.html', title = 'Sign in', form=form)