### utils/business_rules.py
from typing import Dict, Any
from sqlalchemy.orm import Session
from config.logging_config import get_logger

logger = get_logger(__name__)


class RoomBusinessRules:
    """Business rules for room operations"""

    async def validate_room_creation(self, room_data: Dict[str, Any], db: Session):
        """
        Validate business rules for room creation

        Args:
            room_data: Room data to validate
            db: Database session
        """
        logger.debug("Validating business rules for room creation")

        # Business rule: Eco-suites must have balcony
        if room_data["room_type"] == "eco-suite" and not room_data.get("has_balcony"):
            raise ValueError("Eco-suite rooms must have a balcony")

        # Business rule: Ocean view rooms have higher minimum price
        if room_data.get("has_ocean_view") and room_data["price_per_night"] < 100:
            raise ValueError(
                "Ocean view rooms must have a minimum price of $100 per night"
            )

        # Business rule: Suite capacity validation
        if (
            room_data["room_type"] in ["suite", "eco-suite"]
            and room_data["capacity"] < 2
        ):
            raise ValueError("Suite rooms must have a minimum capacity of 2 guests")

        logger.debug("Business rules validation completed")
