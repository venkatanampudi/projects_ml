import logging
import os
from datetime import datetime

# Create logs folder
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Log file name with timestamp
LOG_FILE = datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s %(name)s:%(lineno)d - %(message)s"
)

# to execute if this code is correct or not.
if __name__ == "__main__":
    logging.info("Logging has started successfully!")

