import os
from flask import request, render_template, redirect
from .blueprint import user
from models.user import User


# 회원가입 페이지 API
@user.route('/form')
def form():
    return render_template('product_form.html')


# 회원가입 API
@user.route('/signup', method=['POST'])
def signup():
    form_data = request.form

    User.insert_one(form_data)
    return "회원가입 성공"


# 테스트 API
@user.route('/test')
def test():
    return "테스트 API입니다."
