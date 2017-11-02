from flask import Blueprint

reporting = Blueprint("reporting", __name__)

reporting.route("/member-report", methods=["GET", "POST"])(report_on_members)
