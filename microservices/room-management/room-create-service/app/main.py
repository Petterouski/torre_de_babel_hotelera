from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager
import uvicorn
from controllers.room_controller import RoomController
from config.database import get_db
from config.logging_config import setup_logging
from middleware.auth_middleware import verify_jwt_token
from middleware.error_handler import setup_error_handlers
from models.room_model import Room
import logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Security
security = HTTPBearer()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    logger.info("Starting room-create-service...")
    yield
    logger.info("Shutting down room-create-service...")


# FastAPI app instance
app = FastAPI(
    title="Room Create Service",
    description="Microservice for creating hotel rooms in eco-friendly hotel management system",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup error handlers
setup_error_handlers(app)

# Initialize controller
room_controller = RoomController()


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "room-create-service"}


@app.post("/api/v1/rooms", status_code=201)
async def create_room(
    room_data: dict,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db=Depends(get_db),
):
    """Create a new room"""
    # Verify JWT token
    user_info = verify_jwt_token(credentials.credentials)

    logger.info(f"Creating room request from user: {user_info.get('user_id')}")

    result = await room_controller.create_room(room_data, db)

    logger.info(f"Room created successfully with ID: {result.get('id')}")
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
