from app import app01, db
from app.models import User, Post


## -- flask shell --> db , User, Post--
@app01.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}