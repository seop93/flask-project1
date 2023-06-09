from flask import Flask, redirect, url_for


from controllers.product import product
from controllers.user import user


app = Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(product, url_prefix='/products')
app.register_blueprint(user, url_prefix='/users')


@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for('product.get_products'))


if __name__ == '__main__':
    app.run(debug= True)

