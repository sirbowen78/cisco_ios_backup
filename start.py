from filehandler import csv_to_dict, dst_file_dir
from ciscoios import export_config
from concurrent.futures import ThreadPoolExecutor
from config import CSV_FILENAME

if __name__ == "__main__":
    devices = csv_to_dict(CSV_FILENAME)
    dst_file_dir()
    with ThreadPoolExecutor(len(devices)) as executor:
        executor.map(export_config, devices)
