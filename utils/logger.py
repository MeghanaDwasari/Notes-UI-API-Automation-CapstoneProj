import logging
import os


LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


LOG_FILE = os.path.join(LOG_DIR, "execution.log")


def get_logger():

    logger = logging.getLogger("agentic_logger")

    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    logger.propagate = False

    if not logger.handlers:

        file_handler = logging.FileHandler(
            LOG_FILE,
            mode="a",
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger