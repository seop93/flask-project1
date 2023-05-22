import os
from flask import request, render_template, flash, redirect, url_for
from .blueprint import product
from .blueprint import user
from models.user import User


# 회원가입 페이지 API
@user.route('/form')
def form():
    return render_template('user_form.html')


# 회원가입 API
@user.route('/signup', methods=['POST'])
def signup():
    form_data = request.form

    if not form_data['password'] == form_data['password_confirmation']:
        flash('비밀번호가 일치하지 않습니다')
        return render_template('user_form.html')

    if not User.check_email(form_data['email']):
        flash('사용중인 이메일')
        return render_template('user_form.html')

    User.insert_one(form_data)
    return redirect(url_for('product.get_products'))

# 테스트 API
@user.route('/test')
def test():
    return "테스트 API입니다."
