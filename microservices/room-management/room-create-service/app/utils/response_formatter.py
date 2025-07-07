### utils/response_formatter.py
from typing import Dict, Any
from models.room_model import Room
from config.logging_config import get_logger

logger = get_logger(__name__)


class ResponseFormatter:
    """Format responses following DRY principle"""

    def format_room_response(self, room: Room) -> Dict[str, Any]:
        """
        Format room data for API response

        Args:
            room: Room instance

        Returns:
            Formatted response dictionary
        """
        logger.debug(f"Formatting response for room ID: {room.id}")

        return {
            "success": True,
            "message": "Room created successfully",
            "data": room.to_dict(),
        }

    def format_error_response(self, error_message: str) -> Dict[str, Any]:
        """
        Format error response

        Args:
            error_message: Error message

        Returns:
            Formatted error response
        """
        return {"success": False, "message": error_message, "data": None}
