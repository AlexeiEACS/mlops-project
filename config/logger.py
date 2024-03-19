import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(pathname)s - %(message)s',
    filename="./config/logfile.log",
    filemode='a'
)

logger = logging.getLogger(__name__)


def log_info(message):
    logger.info(message)


def log_debug(message):
    logger.debug(message)


def log_error(message):
    logger.error(message)
