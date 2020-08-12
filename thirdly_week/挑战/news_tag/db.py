from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:123456@localhost/shiyanlou'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
client = MongoClient("127.0.0.1", 27017)
mongo_db = client.shiyanlou

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

    def add_tag(self, tag_name):
        """为文章添加标签"""
        mongo_db.tags.insert_one({'name':self.tag_name})

    def remove_tag(self, tag_name):
        """删除文章标签"""
        mongo_db.tags.delete_one({name:self.tag_name})

    @property
    def tags(self):
        return mongo_db.tags.find()

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
