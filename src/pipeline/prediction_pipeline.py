import os
import sys
import pandas as pd
from src.logger.logger import logging
from src.exception.exception import customexception
from src.utils.utils import load_obj

class predictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)

            scaled_features=preprocessor.transform(features)
            pred = model.predict(scaled_features)

            return pred
        
        except Exception as e:
            raise customexception(e, sys)
        
class customData:
    def __init__(self, carat:float, depth:float, table:float, x:float, y:float, z:float, cut:str, color:str, clarity:str):
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
            'carat':[self.carat],
            'depth':[self.depth],
            'table':[self.table],
            'x':[self.x],
            'y':[self.y],
            'z':[self.z],
            'cut':[self.cut],
            'color':[self.color],
            'clarity':[self.clarity]
            }

            df =pd.DataFrame(custom_data_input_dict)
            logging.info(f"Dataframe gathered head: \n{df.head().to_string()}")

            return df

        except Exception as e:
            raise customexception(e, sys)