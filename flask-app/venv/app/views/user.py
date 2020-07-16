from flask import render_template, request
from app.models.user import User, _create
class views:
    def index():
        return render_template('users/index.html')
    def new():
        return render_template('users/new.html')
    def create():
        username = request.form['username']
        email = request.form['email']
        #call models
        _create(username, email)
        return "User creation seccessful"