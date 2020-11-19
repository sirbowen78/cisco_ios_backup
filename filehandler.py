import csv
from config import DST_DIR
import os
from logger import init_log

log = init_log()


def csv_to_dict(csv_file: str) -> list:
    """
    This function reads the content from csv file, then converts to dictionary.
    Each dictionary is appended to a list.
    :param csv_file: absolute path of csv file, must be a string.
    :return: list of dictionaries.
    """
    devices = []
    with open(csv_file, "r") as f:
        log.info(f"Reading content from {csv_file}")
        reader = csv.DictReader(f)
        for row in reader:
            log.info("Converting contents to dictionary")
            devices.append(row)
        log.info("Conversion completed.")
    return devices


def dst_file_dir():
    """
    Check if the destination directory exists or not, if not create it/them.
    :return:
    """
    if not os.path.exists(DST_DIR):
        log.info(f"Creating {DST_DIR}.")
        os.makedirs(DST_DIR, 0o666)
