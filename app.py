from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root123@localhost/school_sys"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    cgpa = db.Column(db.Float, default=0.0)

    is_active = db.Column(db.Boolean, default=True)

    joined_date = db.Column(db.Date, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)



    

@app.route("/")
def home():
    return jsonify({
        "message": "Flask + MySQL Connected Successfully"
    })

@app.route("/api/students", methods=["POST"])
def create_student():

    data = request.get_json()

        

    if not data:
            return jsonify({ "error": "No input data provided"}), 400

    if not data.get("full_name"):
            return jsonify({"error": "Full name is required"}), 400

    if not data.get("email"):
            return jsonify({"error": "Email is required"}), 400

    if not data.get("age"):
            return jsonify({"error": "Age is required"}), 400

    if int(data["age"]) <= 0:
            return jsonify({"error": "Age must be a positive integer"}), 400

    if not data.get("joined_date"):
            return jsonify({"error": "Joined date is required"}), 400

        

        