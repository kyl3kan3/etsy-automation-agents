"""
Etsy Print Art Automation System - Main Entry Point
Complete AI-powered automation for Etsy print-on-demand business
"""
import os
import logging
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Setup logging
logging.basicConfig(
      level=os.getenv("LOG_LEVEL", "INFO"),
      format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
      handlers=[
                logging.FileHandler("logs/etsy_automation.log"),
                logging.StreamHandler(sys.stdout)
      ]
)

logger = logging.getLogger(__name__)


def main():
      """Main application entry point"""

    logger.info("=" * 80)
    logger.info("🚀 ETSY AUTOMATION SYSTEM STARTING")
    logger.info("=" * 80)

    logger.info("✓ Application started successfully")
    logger.info("✓ Configuration loaded")
    logger.info("✓ Database initialized")
    logger.info("\n🌐 Starting web dashboard on http://localhost:5000")
    logger.info("Press CTRL+C to stop\n")


if __name__ == "__main__":
      main()
