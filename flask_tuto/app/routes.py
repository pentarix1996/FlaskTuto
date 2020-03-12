from flask import render_template
from app import app01

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
			'body':		'La pésima noticia de Juan'
		}
	]
	return render_template('index.html', title='home', user=user, posts=posts)
