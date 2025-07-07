from ..repositories.room_repository import RoomRepository
from ..utils.logger import logger


class RoomService:
    def __init__(self):
        self.room_repo = RoomRepository()

    def list_rooms(self):
        return self.room_repo.fetch_all_rooms()

    def get_room(self, room_id):
        return self.room_repo.fetch_room_by_id(room_id)
