import logging
import os
from datetime import datetime


LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


log_file = os.path.join(
    LOG_DIR,
    f"arogya_{datetime.now().strftime('%Y%m%d')}.log"
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)


def get_logger(name: str):
    return logging.getLogger(name)