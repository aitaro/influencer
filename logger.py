import os
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-7s %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)
logger = logging.getLogger(__name__)
