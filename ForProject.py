from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/flask_app_db'
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)


@app.route("/", methods=["GET", "POST"])
def hello():
    return render_template("reg.html")


@app.route("/reg_run", methods=["GET", "POST"])
def visual():
    name = request.form["name"]
    surname = request.form["surname"]
    email = request.form["e-mail"]
    password = request.form["password"]
    print(name, surname, email, password)
    return redirect("/")


app.run(debug=True)
