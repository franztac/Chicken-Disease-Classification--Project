import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Step 1: Create the parent directory if it doesn't exist
    if filedir != "":
        logging.info(f"Creating folder: {filedir} for file: {filename}")
        os.makedirs(filedir, exist_ok=True)

    # Step 2: Create the file if it doesn't exist or is empty
    if not filepath.exists():
        logging.info(f"Creating file: {filepath}")
        with open(filepath, "w") as f:
            pass  # Creating an empty file

    elif filepath.stat().st_size == 0:
        # The file exists but is empty, so we create it again (or leave it empty)
        logging.info(f"File exists but is empty: {filepath}")
        with open(filepath, "w") as f:
            pass  # Creating an empty file again (or leaving it empty)

    else:
        logging.info(f"File: {filepath} already exists and is not empty")
