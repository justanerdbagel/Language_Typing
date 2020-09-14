# from flask import Flask, render_template, flash, redirect, url_for
# from app.config import Config
# from app.forms import LoginForm
#
# app = Flask(__name__)
# app.config.from_object(Config)
from app import app, db


# user = {'username': 'bobby'}
# posts = [{
#         'author': {'username': 'John'},
#         'body': 'Beautiful day in Portland!'
#         },
#         {
#         'author': {'username': 'Susan'},
#         'body': 'The Avengers movie was so cool!'
#         }
#         ]

#
# @app.route('/')
# def home():
#
#     return render_template('home.html', user=user, posts=posts)
#
#
# @app.route('/blog')
# def blog():
#     return render_template("blog.html", user=user, posts=posts)
#
#
# @app.route('/type_stuff')
# def type_stuff():
#     return render_template("type_stuff.html", user=user)
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect(url_for('index'))
#     return render_template("login.html", title="Sign In", form=form)
#
#
if __name__ == '__main__':
    app.run()
