from typing import Dict, Any
from sqlalchemy.orm import Session
from models.room_model import Room
from repositories.room_repository import RoomRepository
from utils.business_rules import RoomBusinessRules
from config.logging_config import get_logger

logger = get_logger(__name__)


class RoomService:
    """Service layer for room business logic"""

    def __init__(self):
        self.room_repository = RoomRepository()
        self.business_rules = RoomBusinessRules()

    async def create_room(self, room_data: Dict[str, Any], db: Session) -> Room:
        """
        Create a new room with business logic validation

        Args:
            room_data: Validated room data
            db: Database session

        Returns:
            Created room instance
        """
        try:
            logger.info("Processing room creation in service layer")

            # Apply business rules
            await self.business_rules.validate_room_creation(room_data, db)

            # Check if room number already exists
            existing_room = await self.room_repository.get_by_room_number(
                room_data["room_number"], db
            )

            if existing_room:
                logger.warning(f"Room number {room_data['room_number']} already exists")
                raise ValueError(
                    f"Room number {room_data['room_number']} already exists"
                )

            # Create room
            room = Room(**room_data)
            created_room = await self.room_repository.create(room, db)

            logger.info(f"Room created in database with ID: {created_room.id}")
            return created_room

        except ValueError:
            raise
        except Exception as e:
            logger.error(f"Error in room service: {str(e)}")
            raise
