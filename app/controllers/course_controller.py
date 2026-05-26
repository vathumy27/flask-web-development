from flask import request, jsonify

from app import db
from app.models.course_model import Course


def create_course():

    try:

        data = request.get_json()

        course = Course(
            course_title=data["course_title"],
            course_fee=data["course_fee"],
            duration_months=data["duration_months"],
            description=data.get("description")
        )

        db.session.add(course)
        db.session.commit()

        return jsonify({
            "message": "Course created successfully"
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500



def get_courses():

    courses = Course.query.all()

    output = []

    for course in courses:

        output.append({
            "id": course.id,
            "course_title": course.course_title,
            "course_fee": course.course_fee
        })

    return jsonify(output)



def get_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({
            "error": "Course not found"
        }), 404

    return jsonify({
        "id": course.id,
        "course_title": course.course_title,
        "course_fee": course.course_fee
    })



def update_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({
            "error": "Course not found"
        }), 404

    data = request.get_json()

    if "course_title" in data:
        course.course_title = data["course_title"]

    if "course_fee" in data:
        course.course_fee = data["course_fee"]

    if "duration_months" in data:
        course.duration_months = data["duration_months"]

    db.session.commit()

    return jsonify({
        "message": "Course updated successfully"
    })



def delete_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({
            "error": "Course not found"
        }), 404

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "message": "Course deleted successfully"
    })