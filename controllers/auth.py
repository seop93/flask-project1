
from flask import flash, redirect, url_for, session
from models.user import User


def check_login():
    if not session.get('user_id'):
        return False

    user = User.find_one(session['user_id'])

    return user


def redirect_to_signin_form():
    flash('로그인을 해주세요')
    return redirect(url_for('user.signin_form'))


def is_admin():
    user = check_login()
    if not user:
        return False

    return user.get('is_admin', False) # default는 None 인수로 지정하면 False로 대체 가능