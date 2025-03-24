from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.vizualization import DataVizualization
from src.utils import kmean_elbo
from src.components.summary import DataSummary
from src.components.data_outliers import DataOutlier
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans



pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 200)
pd.set_option('display.float_format', lambda x: '%.2f' % x)


if __name__ == "__main__":
    #data ingestion   
    data_file_path = r"data\AW_custSummary.csv"
    ing_obj = DataIngestion()
    data = ing_obj.initiate_data_ingestion(data_file_path)
    # Replace NaN values with 0
    data.fillna(0, inplace=True)
    print(data.head())
 
    num_cols = data[['num_uniq_orders','orderFrequency','daysSinceLastOrder','num_uniq_products','reorder_ratio','TotalRevenue']]
    cat_cols = data[[]]
    rm_cols = data[['CustomerID']]

    trans_obj =  DataTransformation()
    scaled_features = trans_obj.initiate_data_transformation(data, num_cols, cat_cols, rm_cols)
    print(scaled_features.shape)
 
    inertia = kmean_elbo(scaled_features, 11)

    viz_obj = DataVizualization()
    viz_obj.plot_elbo_curve(inertia, 11)
  
    # Choose the optimal number of clusters (e.g., k=5)
    kmeans = KMeans(n_clusters=5, random_state=100)
    data['cluster'] = kmeans.fit_predict(scaled_features)

    # Display cluster distribution
    print(data['cluster'].value_counts())

    # Group by cluster and analyze mean values
    cluster_summary = data.groupby('cluster').mean()
    print(cluster_summary)
    exit()
    first_customers = data.head(1000)

    viz_obj.plot_segementation(first_customers, "num_uniq_orders", "daysSinceLastOrder", "cluster",
                                "Customer Segmentation: Total Orders vs Days since last order")


   