from flask import request, render_template, flash, redirect, url_for, session
from .auth import check_login, redirect_to_signin_form
from .blueprint import user
from models.user import User
from .auth import is_admin


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


# 로그인 API
@user.route('/signin', methods=['POST'])
def signin():
    form_data = request.form
    user = User.sign_in(form_data)

    if not user:
        flash('이메일 주소 또는 비밀번호를 확인해주세요')
        return render_template('user_signin.html')
    else:
        session['user_id'] = str(user['_id'])
        if is_admin():
            session['is_admin'] = True
        return redirect(url_for('product.get_products'))


# 로그인 페이지 API
@user.route('/signin')
def signin_form():
    return render_template('user_signin.html')


# 로그아웃
# @check_auth 데코레이터 방식도 가능
@user.route('/signout')
def signout():
    user = check_login()
    if not user:
        return redirect_to_signin_form()

    session.pop('user_id', None)
    session.pop('is_admin', None)
    return redirect(url_for('product.get_products'))



@user.route('/test')
def test():
    return "테스트 API입니다록."
