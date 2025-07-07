from flask import Blueprint
from ..controllers.room_controller import get_rooms, get_room_by_id

room_bp = Blueprint("room", __name__)

room_bp.route("/rooms", methods=["GET"])(get_rooms)
room_bp.route("/rooms/<string:room_id>", methods=["GET"])(get_room_by_id)
