from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.room_model import Room
from config.logging_config import get_logger

logger = get_logger(__name__)


class RoomRepository:
    """Repository layer for room data access"""

    async def create(self, room: Room, db: Session) -> Room:
        """
        Create a new room in the database

        Args:
            room: Room instance to create
            db: Database session

        Returns:
            Created room instance
        """
        try:
            logger.debug(f"Creating room in database: {room.room_number}")

            db.add(room)
            db.commit()
            db.refresh(room)

            logger.debug(f"Room saved successfully with ID: {room.id}")
            return room

        except IntegrityError as e:
            logger.error(f"Database integrity error: {str(e)}")
            db.rollback()
            raise ValueError("Room number already exists or violates constraints")
        except Exception as e:
            logger.error(f"Database error creating room: {str(e)}")
            db.rollback()
            raise

    async def get_by_room_number(self, room_number: str, db: Session) -> Optional[Room]:
        """
        Get room by room number

        Args:
            room_number: Room number to search
            db: Database session

        Returns:
            Room instance if found, None otherwise
        """
        try:
            logger.debug(f"Searching for room number: {room_number}")

            room = db.query(Room).filter(Room.room_number == room_number).first()

            if room:
                logger.debug(f"Room found with ID: {room.id}")
            else:
                logger.debug(f"Room not found: {room_number}")

            return room

        except Exception as e:
            logger.error(f"Error querying room: {str(e)}")
            raise
