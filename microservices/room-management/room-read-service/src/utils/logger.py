from loguru import logger
import os

# Elimina el logger por defecto y agrega uno personalizado
logger.remove()
logger.add(
    "logs/room-read-service.log",
    rotation="500 MB",
    level="INFO",
    format="{time} | {level} | {message}",
)
logger.add(lambda msg: print(msg), level="DEBUG")

os.makedirs("logs", exist_ok=True)

# Exporta el logger para usarlo en otros módulos
__all__ = ["logger"]
