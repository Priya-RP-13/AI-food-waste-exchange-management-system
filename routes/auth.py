from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db, bcrypt
from models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        role = request.form["role"]

        # Check if passwords match
        if password != confirm_password:
            return "Passwords do not match!"

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email already registered!"

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Create user
        user = User(
            name=name,
            email=email,
            password=hashed_password,
            role=role
        )

        # Save to database
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth.route("/login")
def login():
    return render_template("auth/login.html")