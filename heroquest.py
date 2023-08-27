from app import app, db
from app.models import User, Hero
from app.api_routes import api_bp


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Hero': Hero}

app.register_blueprint(api_bp, url_prefix='/api')
