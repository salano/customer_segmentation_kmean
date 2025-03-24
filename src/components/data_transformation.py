import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


from src.exception import CustomException
from src.logger import logging


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pk1')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self, numerical_columns, categorical_columns):
        '''
        This function is responsible for the transformation of the numerical and categorical values in the dataset
        '''
        try:

            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )

            logging.info('Numerical values standard scaling completed')

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder', OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )

            logging.info('Categorical values one hot encoding and standard scaling completed')
            # Normalize the data
            '''
            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipeline', cat_pipeline, categorical_columns)
                ]
            )
            '''
            preprocessor = StandardScaler(with_mean=False)
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, data, 
                                     numerical_columns, 
                                        categorical_columns, 
                                        removed_columns):
        try:

            logging.info('Datasets loaded')

            logging.info('Initialize preprocessor object')
            preprocessor_obj = self.get_data_transformation_object(numerical_columns, categorical_columns)

            features_df = data.drop(columns=removed_columns, axis=1)

            logging.info(
                f'Applying preprocessing to dataframes using preprocessor object'
            )

            feature_array = preprocessor_obj.fit_transform(features_df)

            return feature_array

        except Exception as e:
            raise CustomException(e, sys)
