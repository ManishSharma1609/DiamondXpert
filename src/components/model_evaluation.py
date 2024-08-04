import os
import sys
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle 
from dataclasses import dataclass
from src.utils.utils import save_object, evaluate_model
from src.logger.logger import logging
from src.exception.exception import customexception

@dataclass
class modelEvaluationConfig:
    pass

class modelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e, sys)
