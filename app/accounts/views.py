from flask import jsonify

from . import accounts


@accounts.route("/", methods=["GET"])
def main():
    return jsonify(message="Ok")
