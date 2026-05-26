from flask import Blueprint

from app.controllers.course_controller import (
    create_course,
    get_courses,
    get_course,
    update_course,
    delete_course
)

course_bp = Blueprint(
    "course_bp",
    __name__
)

course_bp.route(
    "/api/courses",
    methods=["POST"]
)(create_course)

course_bp.route(
    "/api/courses",
    methods=["GET"]
)(get_courses)

course_bp.route(
    "/api/courses/<int:id>",
    methods=["GET"]
)(get_course)

course_bp.route(
    "/api/courses/<int:id>",
    methods=["PUT"]
)(update_course)

course_bp.route(
    "/api/courses/<int:id>",
    methods=["DELETE"]
)(delete_course)