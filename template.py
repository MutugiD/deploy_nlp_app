import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    f"app/model/__init__.py",
    f"app/model/machine_learning_pipeline.py", 
    f"app/preprocessing/__init__.py",
    f"app/preprocessing/nlp_preprocessing.py",
    f"app/__init__.py",
    f"app/main.py",
    f"app/README.md",
    f"model-dev/data/emotion-labels-test.csv", 
    f"model-dev/data/emotion-labels-train.csv", 
    f"model-dev/data/emotion-labels-vals.csv", 
    f"model-dev/README.md", 
    ".gitignore", 
    "Dockerfile",
    "README.md",
    "build_model.py", 
    "entry.sh",
    "install_requirements.sh",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")