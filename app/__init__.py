from flask import Flask

from app.db_manager import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pinkikki:password@192.168.33.10:5432/hero_test'
db.init_app(app)

from .views import hero

app.register_blueprint(hero.mod)
