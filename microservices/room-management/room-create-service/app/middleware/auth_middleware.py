### middleware/auth_middleware.py
import jwt
from fastapi import HTTPException
from config.logging_config import get_logger
import os

logger = get_logger(__name__)

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-here")


def verify_jwt_token(token: str) -> dict:
    """
    Verify JWT token and return user information

    Args:
        token: JWT token string

    Returns:
        User information from token
    """
    try:
        logger.debug("Verifying JWT token")

        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        if not payload.get("user_id"):
            raise HTTPException(
                status_code=401, detail="Invalid token: missing user_id"
            )

        logger.debug(f"Token verified for user: {payload.get('user_id')}")
        return payload

    except jwt.ExpiredSignatureError:
        logger.warning("Token has expired")
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError as e:
        logger.error(f"Invalid token: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        logger.error(f"Token verification error: {str(e)}")
        raise HTTPException(status_code=401, detail="Authentication failed")
