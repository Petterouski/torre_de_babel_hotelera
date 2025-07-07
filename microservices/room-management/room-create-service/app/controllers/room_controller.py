from typing import Dict, Any
from services.room_service import RoomService
from utils.validators import RoomValidator
from utils.response_formatter import ResponseFormatter
from config.logging_config import get_logger
from fastapi import HTTPException
import logging

# Prueba 4.0 CI
logger = get_logger(__name__)


class RoomController:
    """Controller for room operations following MVC pattern"""

    def __init__(self):
        self.room_service = RoomService()
        self.validator = RoomValidator()
        self.response_formatter = ResponseFormatter()

    async def create_room(self, room_data: Dict[str, Any], db) -> Dict[str, Any]:
        """
        Create a new room with validation and error handling

        Args:
            room_data: Dictionary containing room information
            db: Database session

        Returns:
            Dictionary with created room data
        """
        try:
            logger.info("Starting room creation process")

            # Validate input data
            validated_data = self.validator.validate_room_data(room_data)
            logger.debug(f"Room data validated: {validated_data}")

            # Create room through service
            created_room = await self.room_service.create_room(validated_data, db)

            # Format response
            response = self.response_formatter.format_room_response(created_room)

            logger.info(f"Room created successfully with ID: {created_room.id}")
            return response

        except ValueError as e:
            logger.error(f"Validation error: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            logger.error(f"Unexpected error creating room: {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")
