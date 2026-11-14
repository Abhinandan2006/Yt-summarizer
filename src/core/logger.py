"""Logging configuration for YT-RAG."""

import logging
import sys
from typing import Any


def setup_logger(name: str = "yt_rag", level: str = "INFO") -> logging.Logger:
    """Configures and returns a structured logger."""
    logger = logging.getLogger(name)

    # Avoid duplicate handlers if already configured
    if logger.handlers:
        return logger

    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(numeric_level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(numeric_level)

    # Clean, informative console log format
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-7s | %(name)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False

    return logger


# Global root logger instance
logger = setup_logger()

