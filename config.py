import os

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MONGO_URL = os.getenv("MONGO_URL")

    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    FORCE_SUB = os.getenv("FORCE_SUB", "")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))

    MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4GB
