from flask import Blueprint


datamarket = Blueprint(
    "datamarket", __name__)


def page():
    return "Hello, datamarket!"


datamarket.add_url_rule(
    "/datamarket/page", view_func=page)


def get_blueprints():
    return [datamarket]
