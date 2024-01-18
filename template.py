import os
from pathlib import Path
import logging
list_of_files=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/transformation.py",
    "src/components/model_evaluation.py",
    "src/pipline/__init__.py",
    "src/pipline/training_pipline.py",
    "src/pipline/prediction_pipline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "scr/exception/exception",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for file_path in list_of_files:
    file_path=Path(file_path)
    filedir,filename= os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Create dictinary: {filedir} for file:{filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass  # create empaty file
