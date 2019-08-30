"""
Authentication views.
"""

from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, logout_user, login_user

from app import models, db
from app.forms import LoginForm, RegistrationForm
from . import bp


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = models.User(username=form.username.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Successfully registered')

        return redirect(url_for('auth_blueprint.login'))

    return render_template('register.html', form=form)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index_blueprint.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth_blueprint.login'))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next', url_for('index_blueprint.index'))

        return redirect(next_page)

    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index_blueprint.index'))
