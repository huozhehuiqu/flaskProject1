from flask import jsonify

from lib.redprint import Redprint

# create redprint
user_redprint = Redprint("user")


@user_redprint.route("/")
def user():
    return jsonify({"type": "user"})
