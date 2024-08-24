import os
import sys
from src.logger.logger import logging
from src.exception.exception import customexception
import pandas as pd

from src.components.data_ingestion import dataIngestion
from src.components.data_transformation import dataTransformation
from src.components.model_trainer import modelTrainer
from src.components.model_evaluation import modelEvaluation

# obj = dataIngestion()

# train_data_path,test_data_path=obj.initiate_data_ingestion()

# data_Transformation  = dataTransformation()

# train_arr,test_arr = data_Transformation.initiate_data_transformation(train_data_path, test_data_path)

# model_Trainer = modelTrainer()

# model_Trainer.initiate_model_training(train_arr, test_arr)

# model_evaluation = modelEvaluation()

# model_evaluation.initiate_model_evaluation(train_arr, test_arr)

class TrainingPipeline:
    def start_data_Ingestion(self):
        try:
            data_Ingestion = dataIngestion()
            train_data_path, test_data_path = data_Ingestion.initiate_data_ingestion()
            return train_data_path, test_data_path
        except Exception as e:
            logging.info(e, sys)

    def start_data_transformation(self, train_data_path, test_data_path):
        try:
            data_Transformation = dataTransformation()
            train_arr, test_arr = dataTransformation.initiate_data_transformation(train_data_path, test_data_path)
            return train_arr, test_arr
        
        except Exception as e:
            logging.info(e, sys)

    def start_model_training(self, train_arr, test_arr):
        try:
            model_trainer = modelTrainer()
            model_trainer.initiate_model_training(train_arr, test_arr)
        
        except Exception as e:
            logging.info(e, sys)

    def start_training(self):
        try:
            train_data_path, test_data_path = self.start_data_Ingestion()
            train_arr, test_arr = self.start_data_transformation(train_data_path, test_data_path)
            self.start_model_training(train_arr, test_arr)

        except Exception as e:
            logging.info(e,sys)

