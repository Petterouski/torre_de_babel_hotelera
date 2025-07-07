## tests/test_room_creation.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from config.database import get_db
from models.room_model import Base
import os

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_room_success():
    """Test successful room creation"""
    room_data = {
        "room_number": "101",
        "room_type": "single",
        "floor": 1,
        "price_per_night": 75.0,
        "capacity": 1,
        "has_balcony": False,
        "has_ocean_view": False,
    }

    # Mock JWT token for testing
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidGVzdF91c2VyIn0.test_signature"

    response = client.post(
        "/api/v1/rooms", json=room_data, headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 201
    data = response.json()
    assert data["success"] is True
    assert data["data"]["room_number"] == "101"


def test_create_room_validation_error():
    """Test room creation with validation errors"""
    room_data = {
        "room_number": "",  # Invalid empty room number
        "room_type": "invalid_type",
        "floor": 0,  # Invalid floor
        "price_per_night": -10,  # Invalid price
        "capacity": 0,  # Invalid capacity
    }

    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidGVzdF91c2VyIn0.test_signature"

    response = client.post(
        "/api/v1/rooms", json=room_data, headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 400


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
