from flask import Blueprint
from api.v1.admin.endpoint import admin_redprint
from api.v1.user.endpoint import user_redprint


def create_blueprint_v1():
    # create blueprint
    v1_blueprint = Blueprint("v1", __name__, url_prefix="/api/v1")

    # register redprint
    admin_redprint.register(bp=v1_blueprint, url_prefix="/admin")
    user_redprint.register(bp=v1_blueprint, url_prefix="/user")

    return v1_blueprint