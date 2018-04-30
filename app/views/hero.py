from flask import Blueprint, render_template, request

from app import db_manager
from app.db_manager import Bug

mod = Blueprint('hero', __name__)


@mod.route('/', methods=['GET'])
def index():
    return render_template("hero/register.html")


@mod.route('/register', methods=['POST'])
def register():
    scene_name = request.form['scene_name']
    content = request.form['content']
    print(f'scene_name:{scene_name},content:{content}')

    bug = Bug(scene_name, content)
    bug.insert()
    db_manager.commit()

    return render_template("hero/register.html")


@mod.route('/delete', methods=['POST'])
def delete():
    bug = Bug.query.get(request.form['id'])
    bug.delete()
    db_manager.commit()


@mod.route('/show', methods=['GET'])
def show():
    bugs = Bug.query.all()
    return render_template("hero/show.html", bugs=bugs)
