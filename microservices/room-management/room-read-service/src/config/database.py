import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
from ..utils.logger import logger

load_dotenv()


def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "hotel_ecoapp"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "password"),
            port=os.getenv("DB_PORT", "5432"),
            cursor_factory=RealDictCursor,
        )
        logger.info("✅ Conexión a base de datos PostgreSQL establecida")
        return conn
    except Exception as e:
        logger.error(f"❌ Error al conectar con PostgreSQL: {e}")
        raise
