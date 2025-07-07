from ..models.room_model import RoomModel
from ..utils.logger import logger


class RoomRepository:
    def __init__(self):
        self.room_model = RoomModel()

    def fetch_all_rooms(self):
        return self.room_model.get_all_rooms()

    def fetch_room_by_id(self, room_id):
        return self.room_model.get_room_by_id(room_id)
