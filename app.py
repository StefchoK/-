from flask import Flask
from flask_cors import CORS
from extensions import db, jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'

CORS(app)
db.init_app(app)
jwt.init_app(app)

from auth_routes import auth_bp
from product_routes import product_bp
from comment_routes import comment_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(product_bp, url_prefix='/api/products')
app.register_blueprint(comment_bp, url_prefix='/api/products')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)