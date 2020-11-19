from pathlib import Path
from datetime import datetime

# Change the RSA private key absolute path here.
RSA_PRIVATE_KEY = str(Path.home()) + "/.ssh/id_rsa"

# Change the parent directory here.
PARENT_DIR = "D:/tmp"

# Change the csv filename path here.
CSV_FILENAME = "D:/tmp/devices.csv"

# Sub directory which uses the current date as name
SUB_DIR = datetime.now().strftime("%Y-%m-%d")

# Destination directory, DO NOT CHANGE THIS.
DST_DIR = f"{PARENT_DIR}/{SUB_DIR}"
