import os
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(message)s]: %(message)s"
log_dir = "./logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # sends logs into the file in the filepath
        logging.StreamHandler(sys.stdout),  # prints logs in the terminal
    ],
)

logger = logging.getLogger("IPYNBrenderer")
