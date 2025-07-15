from flask import Blueprint, render_template
from .models import Product


main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/')
@main.route('/index/')
def index():
    products = Product.query.all()
    return render_template('index.html',products=products)

@main.route('/result/')
def result():
    products = Product.query.all()
    return render_template('result.html',products=products)

@main.route('/result/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('result.html', product=product)

@main.route('/about/')
def about():
    return render_template('about.html')

@main.route('/contact/')
def contact():
    return render_template('contact.html')

@main.route('/login/')
def login():
    return render_template('login.html')


# if __name__ == "__main__":
#     app.run()