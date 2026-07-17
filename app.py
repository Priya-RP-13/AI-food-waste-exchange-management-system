from flask import Flask
from config import Config
from extensions import db, bcrypt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)

from models.user import User

with app.app_context():
    db.create_all()

from routes.auth import auth
app.register_blueprint(auth)

@app.route("/")
def home():
    return "<h1>Welcome to AI Food Waste Exchange System</h1>"

if __name__ == "__main__":
    app.run(debug=True)