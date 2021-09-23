from flask import jsonify

from lib.redprint import Redprint

# create redprint
admin_redprint = Redprint("admin")


@admin_redprint.route("/")
def admin():
    return jsonify({"type": "admin"})