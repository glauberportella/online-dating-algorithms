from init_params import (gen_bool_tup, gen_cat_dict, gen_date_dict,
                         gen_list_dict, gen_ord_dict)
from numpy.random import random, randint
from random import choice, sample
from rand_time import randomDate


class DataCluster:
    # Initialize consistent parameters
    def __init__(self, sample_count):
        self.bool_tup = gen_bool_tup()
        self.cat_dict = gen_cat_dict()
        self.date_dict = gen_date_dict()
        self.list_dict = gen_list_dict()
        self.ord_dict = gen_ord_dict()
        self.sample_count = sample_count

    # Boolean Cluster - Non depend on another
    def init_bool_cluster(self):
        self.bool_cluster = {
            key: randint(0, 2, self.sample_count)
            for key in self.bool_tup
        }

    # Categorical Cluster - One hot: Only one from a subset
    def init_cat_cluster(self):
        self.cat_cluster = {
            key: [choice(val) for i in range(self.sample_count)]
            for key, val in self.cat_dict.items()
        }

    # Date Cluster - Temporal
    def init_date_cluster(self):
        self.date_cluster = {
            key: [
                randomDate(val[0], val[1], random())
                for i in range(self.sample_count)
            ]
            for key, val in self.date_dict.items()
        }

    # List Cluster - Can include 0 or more
    def init_list_cluster(self):
        self.list_cluster = {
            key: [
                sample(val, randint(0, len(val)))
                for i in range(self.sample_count)
            ]
            for key, val in self.list_dict.items()
        }

    # Ordinal Cluster - Numerical
    def init_ord_cluster(self):
        self.ord_cluster = {
            key: [randint(val[0], val[1]) for i in range(self.sample_count)]
            for key, val in self.ord_dict.items()
        }

    # Initialize all subclusters
    def init_all_clusters(self):
        self.init_bool_cluster()
        self.init_cat_cluster()
        self.init_date_cluster()
        self.init_list_cluster()
        self.init_ord_cluster()

    # Merge all subclusters above
    def merge_clusters(self):
        self.merged_cluster = {
            **self.bool_cluster,
            **self.cat_cluster,
            **self.date_cluster,
            **self.list_cluster,
            **self.ord_cluster
        }
