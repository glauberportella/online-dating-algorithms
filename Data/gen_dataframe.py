from DataCluster import DataCluster
from pandas import DataFrame
"""
The dataset will be organized into various
clusters with clear biases.

The outline is provided below:

Cluster 1 - Random Data Cluster
"""

# Create a random cluster instance of 10000 samples
rand_cluster = DataCluster(10000)

# Initialize each sub-cluster
rand_cluster.init_all_clusters()
rand_cluster.merge_clusters()
rand_df = DataFrame(rand_cluster.merged_cluster)
