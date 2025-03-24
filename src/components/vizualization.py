import os
import sys
from src.exception import CustomException
from src.logger import logging

import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 15, 5
import seaborn as sns
sns.set_style("whitegrid")


class DataVizualization:
    def __init__(self):
        pass

    def plot_elbo_curve(self, inertia_data, n: int = 12):
        logging.info('Entered data vizualization component')
        try:
            plt.plot(range(1, n), inertia_data, marker='o')
            plt.xlabel('Number of Clusters')
            plt.ylabel('Inertia')
            plt.title('Elbow Method')
            plt.show()
                            
            return None
        except Exception as e:
            raise CustomException(e, sys)
        
    def plot_segementation(self, data, value_1, value_2, cluster_name, p_title):
        logging.info('Entered data vizualization component')
        try:
            plt.figure(figsize=(10, 6))
            plt.scatter(
                data[value_1],
                data[value_2],
                c=data[cluster_name],
                cmap='viridis',
                alpha=0.6
            )
            plt.title(p_title)
            plt.xlabel(value_1)
            plt.ylabel(value_2)
            plt.colorbar(label='Cluster')
            plt.show()
                            
            return None
        except Exception as e:
            raise CustomException(e, sys)
        
        
   