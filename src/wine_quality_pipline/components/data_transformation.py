import os
import urllib.request as request
from src.wine_quality_pipline import logger
import zipfile
from src.wine_quality_pipline.entity.config_entity import (DataTransformationConfig)
import pandas as pd
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir , "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir , "test.csv"), index=False)

        logger.info(f"Train and Test data saved.")
        logger.info(f"Train data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")
