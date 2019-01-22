from init_params import gen_bool_tup, gen_cat_dict, gen_list_dict
from numpy.random import random, randint
from random import choice, sample
from time import localtime, mktime, strptime, strftime


class DataCluster:
    # Initialize consistent parameters
    def __init__(self, sample_count):
        self.bool_tup = gen_bool_tup()
        self.cat_dict = gen_cat_dict()
        self.list_dict = gen_list_dict()
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
            key:
            [choice(self.cat_dict[key]) for i in range(self.sample_count)]
            for key in self.cat_dict.keys()
        }

    # Date Cluster - Temporal
    def init_date_cluster(self):
        def strTimeProp(start, end, format, prop):
            stime = mktime(strptime(start, format))
            etime = mktime(strptime(end, format))
            ptime = stime + prop * (etime - stime)
            return strftime(format, localtime(ptime))

        def randomDate(start, end, prop):
            return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

        def init_join_date(self):
            self.join_date = randomDate("1/1/2017 12:00 AM",
                                        "1/1/2018 12:00 AM", random())

        def dates_to_dict(self):
            self.date_cluster = {
                key: [
                    randomDate("1/1/2018 12:00 AM", "1/1/2019 12:00 AM",
                               random()) for i in range(self.sample_count)
                ]
                for key in ("last_like_time", "last_swipe_time",
                            "last_match_time", "last_online_time",
                            "last_message_time")
            }
            self.date_cluster["join_date"] = [
                randomDate("1/1/2017 12:00 AM", "1/1/2018 12:00 AM", random())
                for i in range(self.sample_count)
            ]

        dates_to_dict(self)

    # List Cluster - Can include 0 or more
    def init_list_cluster(self):
        self.list_cluster = {
            key: [
                sample(self.list_dict[key], randint(0,
                                                    len(self.list_dict[key])))
                for i in range(self.sample_count)
            ]
            for key in self.list_dict.keys()
        }

    # Ordinal Cluster - Numerical
    def init_ord_cluster(self):
        self.ord_cluster = {}

        def init_id(self):
            self.ord_cluster["id"] = [
                randint(1000000, 9999999) for i in range(self.sample_count)
            ]

        def init_age(self):
            self.ord_cluster["age"] = [
                randint(18, 36) for i in range(self.sample_count)
            ]

        def init_height_in(self):
            self.ord_cluster["height_in"] = [
                randint(56, 78) for i in range(self.sample_count)
            ]

        def init_weight_lbs(self):
            self.ord_cluster["weight_lbs"] = [
                randint(90, 300) for i in range(self.sample_count)
            ]

        def init_days_btwn_last(self):
            for key in ("days_btwn_last_like", "days_time_btwn_last_swipe",
                        "days_btwn_last_match", "days_btwn_last_online",
                        "days_btwn_last_message"):
                self.ord_cluster[key] = [
                    randint(0, 365) for i in range(self.sample_count)
                ]

        def init_totals(self):
            for key in ("total_swipes", "total_likes", "total_time_online_hrs",
                        "total_messages", "total_matches"):
                self.ord_cluster[key] = [
                    randint(0, 1000) for i in range(self.sample_count)
                ]

        def init_avgs(self):
            for key in ("avg_matches_per_month", "avg_swipes_per_month",
                        "avg_likes_per_month", "avg_hrs_per_month",
                        "avg_messages_per_month"):
                self.ord_cluster[key] = [
                    randint(0, 100) for i in range(self.sample_count)
                ]

        def init_total_matches_msgd(self):
            self.ord_cluster["total_matches_msgd"] = [
                randint(0, 200) for i in range(self.sample_count)
            ]

        def init_pic_count(self):
            self.ord_cluster["pic_count"] = [
                randint(4, 11) for i in range(self.sample_count)
            ]

        def init_bio_word_count(self):
            self.ord_cluster["bio_word_count"] = [
                randint(0, 500) for i in range(self.sample_count)
            ]

        init_id(self)
        init_age(self)
        init_height_in(self)
        init_weight_lbs(self)
        init_days_btwn_last(self)
        init_totals(self)
        init_avgs(self)
        init_total_matches_msgd(self)
        init_pic_count(self)
        init_bio_word_count(self)

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
