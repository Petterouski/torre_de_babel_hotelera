### middleware/error_handler.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from config.logging_config import get_logger

logger = get_logger(__name__)


def setup_error_handlers(app):
    """Setup global error handlers"""

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"success": False, "message": exc.detail, "data": None},
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unexpected error: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal server error",
                "data": None,
            },
        )
