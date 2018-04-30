# from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Bug(db.Model):
    __tablename__ = 'bug'
    id = db.Column(db.Integer, primary_key=True)
    scene_name = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, scene_name, content):
        self.scene_name = scene_name
        self.content = content

    def insert(self):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)


def commit():
    db.session.commit()
