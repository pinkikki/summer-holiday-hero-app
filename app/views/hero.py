from flask import Blueprint, render_template

mod = Blueprint('hero', __name__)


@mod.route('/')
def index():
  return render_template("hero/index.html")
