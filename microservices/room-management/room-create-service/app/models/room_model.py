from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, func
from sqlalchemy.orm import declarative_base, DeclarativeMeta
from datetime import datetime

Base: DeclarativeMeta = declarative_base()


class Room(Base):
    """Room model for database operations"""

    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String(10), unique=True, index=True, nullable=False)
    room_type = Column(String(50), nullable=False)  # single, double, suite, eco-suite
    floor = Column(Integer, nullable=False)
    price_per_night = Column(Float, nullable=False)
    capacity = Column(Integer, nullable=False)
    has_balcony = Column(Boolean, default=False)
    has_ocean_view = Column(Boolean, default=False)
    is_available = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def to_dict(self):
        """Convert room instance to dictionary"""
        return {
            "id": self.id,
            "room_number": self.room_number,
            "room_type": self.room_type,
            "floor": self.floor,
            "price_per_night": self.price_per_night,
            "capacity": self.capacity,
            "has_balcony": self.has_balcony,
            "has_ocean_view": self.has_ocean_view,
            "is_available": self.is_available,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
