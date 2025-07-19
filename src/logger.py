"""
Logger setup module.
"""

import logging
import os


def get_logger(name: str) -> logging.Logger:
    """
    Configures and returns a logger instance.

    Args:
        name (str): The logger name.

    Returns:
        logging.Logger: Configured logger.
    """
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        format="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        level=log_level,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(name)
