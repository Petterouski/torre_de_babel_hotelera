### config/logging_config.py
import logging
import logging.handlers
import os
from datetime import datetime


def setup_logging():
    """Setup logging configuration"""

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.handlers.RotatingFileHandler(
                "logs/room-create-service.log", maxBytes=10485760, backupCount=5  # 10MB
            ),
            logging.StreamHandler(),
        ],
    )

    # Set specific log levels
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    logging.getLogger("uvicorn").setLevel(logging.INFO)


def get_logger(name: str) -> logging.Logger:
    """Get configured logger instance"""
    return logging.getLogger(name)
