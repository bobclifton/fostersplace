import os
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "thisisasecret"

# database setup and config
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "foster.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


#orm models
class Politics(db.Model):
    __tablename__ = 'politics'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    link = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)

    def __init__(self, link, name):
        self.link = link
        self.name = name

    def __repr__(self):
        return "<Politics: {}>".format(self.name)

class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    link = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)

    def __init__(self, link, name):
        self.link = link
        self.name = name

    def __repr__(self):
        return "<News: {}>".format(self.name)

class Tech(db.Model):
    __tablename__ = 'tech'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    link = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)

    def __init__(self, link, name):
        self.link = link
        self.name = name

    def __repr__(self):
        return "<Tech: {}>".format(self.name)

#routes

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/news')
def news():
    sites = {}
    news = News.query.order_by(News.name).all()
    for row in news:
            sites.update({row.link : row.name})
    return render_template("news.html", sites=sites)

@app.route('/politics')
def politics():
    sites = {}
    politics = Politics.query.order_by(Politics.name).all()
    for row in politics:
            sites.update({row.link : row.name})
    return render_template("politics.html", sites=sites)

@app.route('/tech')
def tech():
    sites = {}
    tech = Tech.query.order_by(Tech.name).all()
    for row in tech:
            sites.update({row.link : row.name})
    return render_template("tech.html", sites=sites)

@app.route('/social')
def social():
    return render_template("social.html")

@app.route('/music')
def music():
    return render_template("music.html")

@app.route('/italian')
def italian():
    return render_template("italian.html")

@app.route('/science')
def science():
    return render_template("science.html")

@app.route('/history')
def history():
    return render_template("history.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")


if __name__ == '__main__':
    app.run(debug=True)