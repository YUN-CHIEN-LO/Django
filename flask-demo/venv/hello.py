from flask import Flask
from flask import render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique = True)

@app.route('/', methods=['GET', 'POST'])
def test():
    if(request.method == 'POST'):
        # save data
        username = request.form['username']
        email = request.form['email']
        user = User(id=1, username = username, email=email)
        db.session.add(user)
        db.session.commit()
        return "Updated"
    else: 
        return render_template("test.html")

@app.route('/hello')
def hello_world():
    return "Hello"

@app.route('/hello/<username>')
def hello_user(username):
    return "Hello " + username

@app.route('/hello/<int:userid>')
def hello_userid(userid):
    return "Hello id: " + str(userid)

@app.route('/hello/url')
def hello_userurl():
    return "Hello url: " + url_for("hello_world")
