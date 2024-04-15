import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s, [%(levelname)s] in %(name)s: %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == "__main__":
    logger.debug("This is a log entry for debugging.")
    logger.info("This is a log entry for information.")
    logger.warning("This is a log entry for a warning.")
    logger.error("This is a log entry for an error.")
    logger.critical("This is a log entry for a critical error.")
