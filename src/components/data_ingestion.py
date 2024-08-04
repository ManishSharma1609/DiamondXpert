import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class dataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts", "raw.csv")
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path:str = os.path.join("artifacts", "test.csv")

class dataIngestion:
    def __init__(self):
        self.ingestion_config = dataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            data = pd.read_csv("C:\\Users\\Dell\\Downloads\\raw.csv")
            logging.info("Reading a DF")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("I have saved the raw dataset in artifact folder")

            logging.info("Here I have performed train test split")

            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data ingestion part completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info(f"An error occurred during data ingestion: {e}")
            raise customexception(e, sys)

if __name__ == "__main__":
    obj = dataIngestion()

    obj.initiate_data_ingestion()