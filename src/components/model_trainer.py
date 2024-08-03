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

@dataclass
class modelEvaluationConfig:
    pass

class modelEvaluation:
    def __init__(self):
        pass
