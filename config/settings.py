import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
IMAGES_DIR = DATA_DIR / "images"
DATABASE_DIR = DATA_DIR / "database"

# Create directories
for directory in [DATA_DIR, LOG_DIR, IMAGES_DIR, DATABASE_DIR]:
      directory.mkdir(exist_ok=True)

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ETSY_API_KEY = os.getenv("ETSY_API_KEY")
ETSY_SHOP_ID = os.getenv("ETSY_SHOP_ID")
TIKTOK_API_KEY = os.getenv("TIKTOK_API_KEY")
TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")
TIKTOK_CREATOR_ID = os.getenv("TIKTOK_CREATOR_ID")

# Database
DATABASE_URL = f"sqlite:///{DATABASE_DIR}/etsy_automation.db"

# Models
GPT_MODEL = "gpt-4-turbo"
DALLE_MODEL = "dall-e-3"
VISION_MODEL = "gpt-4-vision"

# Image Generation
IMAGE_SIZE = "1024x1024"
IMAGE_QUALITY = "hd"
TARGET_DPI = 300
BATCH_SIZE = 50

# Etsy
ETSY_BASE_URL = "https://api.etsy.com/v3"
ETSY_IMAGE_LIMIT = 10
ETSY_DEFAULT_PRICE = 24.99

# TikTok
TIKTOK_BASE_URL = "https://open.tiktok.com/v1"
TIKTOK_VIDEO_LENGTH = 15
TIKTOK_POSTING_INTERVAL = 86400

# Scheduling
SCHEDULER_TIMEZONE = "UTC"
DAILY_RUN_TIME = "06:00"
BATCH_PROCESSING_INTERVAL = 3600

# Limits & Thresholds
MAX_RETRIES = 3
BACKOFF_FACTOR = 2
TIMEOUT_SECONDS = 30
MIN_IMAGE_QUALITY_SCORE = 0.7
MAX_CONCURRENT_UPLOADS = 5

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
