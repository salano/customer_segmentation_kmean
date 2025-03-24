from src.exception import CustomException
from src.logger import logging
import sys
import numpy as np
import pandas as pd


from sklearn.cluster import KMeans


# Determine the optimal number of clusters using the Elbow Method
def kmean_elbo(scaled_features, n: int = 12):
    try:
        inertia = []
        for k in range(1, n):
            kmeans = KMeans(n_clusters=k, random_state=100)
            kmeans.fit(scaled_features)
            inertia.append(kmeans.inertia_)
        return inertia    
    except Exception as e:
        raise CustomException(e, sys)
    
