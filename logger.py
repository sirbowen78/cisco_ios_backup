import logging


def init_log():
    """
    This function logs the activity to the console.
    :return:
    """
    logger = logging.getLogger(__name__)
    log_fmt = logging.Formatter(
        fmt="%(asctime)s %(funcName)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger.propagate = False
    logger.setLevel(logging.INFO)
    if not logger.hasHandlers():
        console = logging.StreamHandler()
        console.setFormatter(log_fmt)
        logger.addHandler(console)
    return logger
