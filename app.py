from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import text

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


class Course(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    course_title = db.Column(db.String(100), unique=True, nullable=False)
    course_fee = db.Column(db.Float, nullable=False)
    duration_months = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    

@app.route("/")
def home():
    return jsonify({
        "message": "Flask + MySQL Connected Successfully"
    })

@app.route("/api/students", methods=["POST"])
def create_student():

    data = request.get_json()

    try:

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
    
            existing_student = Student.query.filter_by(email=data["email"]).first()

            if existing_student:
             return jsonify({"error": "Email already exists"}), 400
    
            student = Student(full_name=data["full_name"],email=data["email"],age=data["age"],cgpa=data.get("cgpa", 0.0),joined_date=datetime.strptime(data["joined_date"],"%Y-%m-%d").date())

            db.session.add(student)
            db.session.commit()

            return jsonify({
            "message": "Student created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

        



# @app.route("/api/students", methods=["GET"])
# def get_students():

#     students = Student.query.all()

#     output = []

#     for student in students:

#         output.append({
#             "id": student.id,
#             "full_name": student.full_name,
#             "email": student.email,
#             "age": student.age,
#             "cgpa": student.cgpa,
#             "is_active": student.is_active,
#             "joined_date": str(student.joined_date)
#         })

#     return jsonify(output), 200



# @app.route("/api/students", methods=["GET"])
# def get_students():

#     students = Student.query.all()

#     output = []

#     for student in students:

#         output.append({
#             "id": student.id,
#             "full_name": student.full_name,
#             "email": student.email,
#             "age": student.age,
#             "cgpa": student.cgpa,
#             "is_active": student.is_active,
#             "joined_date": str(student.joined_date)
#         })

#     return jsonify(output), 200






# @app.route("/api/students/<int:id>", methods=["GET"])
# def get_student(id):

#     student = Student.query.get(id)

#     if not student:
#         return jsonify({
#             "error": "Student not found"
#         }), 404

#     return jsonify({
#         "id": student.id,
#         "full_name": student.full_name,
#         "email": student.email,
#         "age": student.age,
#         "cgpa": student.cgpa
#     })





# @app.route("/api/students/<int:id>", methods=["PUT"])
# def update_student(id):

#     student = Student.query.get(id)

#     if not student:
#         return jsonify({"error": "Student not found" }), 404

#     data = request.get_json()

#     if not data:
#         return jsonify({"error": "No data provided"}), 400

#     if "full_name" in data:
#         student.full_name = data["full_name"]

#     if "email" in data:

#         existing_email = Student.query.filter(
#             Student.email == data["email"],
#             Student.id != id
#         ).first()

#         if existing_email:
#             return jsonify({"error": "Email already exists"}), 400

#         student.email = data["email"]

#     if "age" in data:

#         if int(data["age"]) <= 0:
#             return jsonify({"error": "Age must be positive"}), 400

#         student.age = data["age"]

#     if "cgpa" in data:
#         student.cgpa = data["cgpa"]

#     db.session.commit()

#     return jsonify({"message": "Student updated successfully"})






# @app.route("/api/students/<int:id>", methods=["DELETE"])
# def delete_student(id):

#     student = Student.query.get(id)

#     if not student:
#         return jsonify({"error": "Student not found"}), 404

#     db.session.delete(student)
#     db.session.commit()

#     return jsonify({"message": "Student deleted successfully"})





if __name__ == "__main__":

    try:

        with app.app_context():

            db.session.execute(text("SELECT 1"))

            print("SUCCESS: Database Connected Successfully")

            db.create_all()

    except Exception as e:

        print("ERROR: Database Connection Failed")

        print(e)

    app.run(debug=True)



