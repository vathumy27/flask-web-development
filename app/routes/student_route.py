from flask import Blueprint

from app.controllers.student_controller import (
    create_student,
    get_students,
    get_student,
    update_student,
    delete_student
)

student_bp = Blueprint(
    "student_bp",
    __name__
)

student_bp.route(
    "/api/students",
    methods=["POST"]
)(create_student)

student_bp.route(
    "/api/students",
    methods=["GET"]
)(get_students)

student_bp.route(
    "/api/students/<int:id>",
    methods=["GET"]
)(get_student)

student_bp.route(
    "/api/students/<int:id>",
    methods=["PUT"]
)(update_student)

student_bp.route(
    "/api/students/<int:id>",
    methods=["DELETE"]
)(delete_student)