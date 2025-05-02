from flask import Blueprint, jsonify, request

calc_bp = Blueprint("calc_routes", __name__)

@calc_bp.route("/calculator/4", methods=["POST"])
def calculator4():
    return jsonify({"message": "Olá mundo"})