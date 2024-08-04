import os
import sys
from src.logger.logger import logging
from src.exception.exception import customexception
import pandas as pd

from src.components.data_ingestion import dataIngestion
from src.components.data_transformation import dataTransformation
from src.components.model_trainer import modelTrainer

obj = dataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()

data_Transformation  = dataTransformation()

train_arr,test_arr = data_Transformation.initiate_data_transformation(train_data_path, test_data_path)

model_Trainer = modelTrainer()

model_Trainer.initiate_model_training(train_arr, test_arr)