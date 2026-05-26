from flask import request, jsonify
from datetime import datetime

from app import db
from app.models.student_model import Student


def create_student():

    try:

        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data"}), 400

        existing_student = Student.query.filter_by(
            email=data["email"]
        ).first()

        if existing_student:
            return jsonify({
                "error": "Email already exists"
            }), 400

        student = Student(
            full_name=data["full_name"],
            email=data["email"],
            age=data["age"],
            cgpa=data.get("cgpa", 0.0),
            joined_date=datetime.strptime(
                data["joined_date"],
                "%Y-%m-%d"
            ).date()
        )

        db.session.add(student)
        db.session.commit()

        return jsonify({
            "message": "Student created successfully"
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500



def get_students():

    students = Student.query.all()

    output = []

    for student in students:

        output.append({
            "id": student.id,
            "full_name": student.full_name,
            "email": student.email,
            "age": student.age,
            "cgpa": student.cgpa
        })

    return jsonify(output)



def get_student(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify({
        "id": student.id,
        "full_name": student.full_name,
        "email": student.email,
        "age": student.age
    })



def update_student(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({
            "error": "Student not found"
        }), 404

    data = request.get_json()

    if "full_name" in data:
        student.full_name = data["full_name"]

    if "email" in data:
        student.email = data["email"]

    if "age" in data:
        student.age = data["age"]

    if "cgpa" in data:
        student.cgpa = data["cgpa"]

    db.session.commit()

    return jsonify({
        "message": "Student updated successfully"
    })



def delete_student(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({
            "error": "Student not found"
        }), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({
        "message": "Student deleted successfully"
    })