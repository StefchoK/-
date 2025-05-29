from flask import Flask
from database import app, db
from auth_routes import auth_bp
from product_routes import product_bp
from comment_routes import comment_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(comment_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)