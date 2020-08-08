from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:123456@localhost/shiyanlou'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    create_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',uselist=False)
    content = db.Column(db.Text)

    def __init__(self, title, create_time, category, content):
        self.title = title
        self.create_time = create_time
        self.category = category
        self.content = content

    def __repr__(self):
        return "<File: {}>".format(self.title)

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category: {}>".format(self.name)

if __name__ == "__main__":
    db.create_all()
