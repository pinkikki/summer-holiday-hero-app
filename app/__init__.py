from flask import Flask
app = Flask(__name__)


from .views import hero

app.register_blueprint(hero.mod)

# @app.route('/')
# def hello_world():
#   return render_template('index.html')
