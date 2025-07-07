from flask import jsonify, request
from ..services.room_service import RoomService
from ..utils.logger import logger


def get_rooms():
    service = RoomService()
    try:
        rooms = service.list_rooms()
        return jsonify(rooms), 200
    except Exception as e:
        logger.error(f"❌ Error en controlador al listar habitaciones: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def get_room_by_id(room_id):
    service = RoomService()
    try:
        room = service.get_room(room_id)
        if not room:
            return jsonify({"error": "Habitación no encontrada"}), 404
        return jsonify(room), 200
    except Exception as e:
        logger.error(f"❌ Error en controlador al obtener habitación: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
