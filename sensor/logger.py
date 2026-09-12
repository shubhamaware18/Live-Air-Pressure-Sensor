import logging
import os
from datetime import datetime


"""
Logger configuration for the LiveSensor project.

This module configures Python's built-in logging system and creates
a timestamped log file inside the project's `logs` directory.

Example:
    >>> import logging
    >>> logging.info("Application started")
"""

# ---------------------------------------------------------------------------
# Log file configuration
# ---------------------------------------------------------------------------

# Generate a unique log file name using the current date and time.
# The hyphen (-) is used instead of colon (:) because ':' is not allowed
# in Windows file names.
LOG_FILE_NAME = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"


# Get the path of the project's current working directory.
CURRENT_WORKING_DIRECTORY = os.getcwd()


# Create the path for the logs directory.
LOGS_DIRECTORY = os.path.join(
    CURRENT_WORKING_DIRECTORY,
    "logs"
)


# Create the logs directory if it does not already exist.
# exist_ok=True prevents an error if the directory already exists.
os.makedirs(LOGS_DIRECTORY, exist_ok=True)


# Create the complete path for the log file.
LOG_FILE_PATH = os.path.join(
    LOGS_DIRECTORY,
    LOG_FILE_NAME
)


# ---------------------------------------------------------------------------
# Logging configuration
# ---------------------------------------------------------------------------

logging.basicConfig(
    filename=LOG_FILE_PATH,

    # Log format:
    # [timestamp] line_number logger_name - log_level - message
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',

    # INFO and higher-level messages will be recorded.
    # Levels:
    # DEBUG < INFO < WARNING < ERROR < CRITICAL
    level=logging.INFO
)