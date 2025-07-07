### utils/validators.py
from typing import Dict, Any
from config.logging_config import get_logger

logger = get_logger(__name__)


class RoomValidator:
    """Validator for room data following DRY principle"""

    VALID_ROOM_TYPES = ["single", "double", "suite", "eco-suite"]

    def validate_room_data(self, room_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate room data input

        Args:
            room_data: Raw room data

        Returns:
            Validated room data
        """
        logger.debug("Validating room data")

        # Required fields validation
        required_fields = [
            "room_number",
            "room_type",
            "floor",
            "price_per_night",
            "capacity",
        ]

        self._validate_required_fields(room_data, required_fields)

        # Specific validations
        validated_data = {
            "room_number": self._validate_room_number(room_data["room_number"]),
            "room_type": self._validate_room_type(room_data["room_type"]),
            "floor": self._validate_floor(room_data["floor"]),
            "price_per_night": self._validate_price(room_data["price_per_night"]),
            "capacity": self._validate_capacity(room_data["capacity"]),
            "has_balcony": room_data.get("has_balcony", False),
            "has_ocean_view": room_data.get("has_ocean_view", False),
            "is_available": room_data.get("is_available", True),
            "is_active": room_data.get("is_active", True),
        }

        logger.debug("Room data validation completed")
        return validated_data

    def _validate_required_fields(self, data: Dict[str, Any], required_fields: list):
        """Validate that all required fields are present"""
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    def _validate_room_number(self, room_number: str) -> str:
        """Validate room number format"""
        if not isinstance(room_number, str) or not room_number.strip():
            raise ValueError("Room number must be a non-empty string")

        room_number = room_number.strip()
        if len(room_number) > 10:
            raise ValueError("Room number cannot exceed 10 characters")

        return room_number

    def _validate_room_type(self, room_type: str) -> str:
        """Validate room type"""
        if not isinstance(room_type, str) or room_type not in self.VALID_ROOM_TYPES:
            raise ValueError(
                f"Room type must be one of: {', '.join(self.VALID_ROOM_TYPES)}"
            )

        return room_type

    def _validate_floor(self, floor: int) -> int:
        """Validate floor number"""
        if not isinstance(floor, int) or floor < 1:
            raise ValueError("Floor must be a positive integer")

        return floor

    def _validate_price(self, price: float) -> float:
        """Validate price per night"""
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price per night must be a positive number")

        return float(price)

    def _validate_capacity(self, capacity: int) -> int:
        """Validate room capacity"""
        if not isinstance(capacity, int) or capacity < 1:
            raise ValueError("Capacity must be a positive integer")

        return capacity
