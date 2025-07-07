from ..config.database import get_db_connection
from ..utils.logger import logger


class RoomModel:
    def __init__(self):
        self.conn = get_db_connection()

    def get_all_rooms(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM rooms")
                rooms = cur.fetchall()
                logger.info(f"📚 Se encontraron {len(rooms)} habitaciones")
                return rooms
        except Exception as e:
            logger.error(f"❌ Error al obtener habitaciones: {e}")
            raise

    def get_room_by_id(self, room_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM rooms WHERE id = %s", (room_id,))
                room = cur.fetchone()
                if room:
                    logger.info(f"📚 Habitación encontrada ID: {room_id}")
                else:
                    logger.warning(f"⚠️ No se encontró la habitación con ID: {room_id}")
                return room
        except Exception as e:
            logger.error(f"❌ Error al buscar habitación por ID: {e}")
            raise
