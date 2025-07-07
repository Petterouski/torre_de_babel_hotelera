from flask import Flask
from src.routes.room_routes import room_bp
from src.utils.logger import logger
import os

app = Flask(__name__)
app.register_blueprint(room_bp)

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 5001))
    logger.info(f"🔌 Iniciando servicio 'room-read-service' en puerto {PORT}")
    app.run(host="0.0.0.0", port=PORT)
