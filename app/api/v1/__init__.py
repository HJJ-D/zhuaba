from flask import Blueprint

from app.api.v1 import session


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    session.api.register(bp_v1)

    return bp_v1
