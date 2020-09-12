from flask import render_template, flash, redirect, url_for
from app import app, forms
# from app.forms import LoginForm
import typing_lang  # temporary import for the mock DB


@app.route('/')
def home():
    return render_template('home.html', user=typing_lang.user, posts=typing_lang.posts)


@app.route('/blog')
def blog():
    return render_template("blog.html", user=typing_lang.user, posts=typing_lang.posts)


@app.route('/type_stuff')
def type_stuff():
    return render_template("type_stuff.html", user=typing_lang.user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)
