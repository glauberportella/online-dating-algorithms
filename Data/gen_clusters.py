from numpy.random import random, randint
from random import choice, sample
from time import localtime, mktime, strptime, strftime


# Boolean Cluster - Non depend on another
def return_bool_cluster(bool_tup):
    return dict(zip(bool_tup, randint(0, 2, len(bool_tup))))


# Categorical Cluster - One hot: Only one from a subset
def return_cat_cluster(cat_dict):
    return {key: choice(cat_dict[key]) for key in cat_dict.keys()}


# Date Cluster - Temporal
def return_date_cluster():
    def strTimeProp(start, end, format, prop):
        stime = mktime(strptime(start, format))
        etime = mktime(strptime(end, format))
        ptime = stime + prop * (etime - stime)
        return strftime(format, localtime(ptime))

    def randomDate(start, end, prop):
        return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

    join_date = randomDate("1/1/2017 12:00 AM", "1/1/2018 12:00 AM", random())

    def dates_to_dict():
        return {
            key: randomDate(join_date, "1/1/2019 12:00 AM", random())
            for key in ("join_date", "last_like_time", "last_swipe_time",
                        "last_match_time", "last_online_time",
                        "last_message_time")
        }

    date_cluster = dates_to_dict()
    date_cluster["join_date"] = join_date
    return date_cluster


# List Cluster - Can include 0 or more
def return_list_cluster(list_dict):
    return {
        key: sample(list_dict[key], randint(0, len(list_dict[key])))
        for key in list_dict.keys()
    }


# Ordinal Cluster - Numerical
def return_ord_cluster():
    return {
        "id": randint(1000000, 9999999),
        "age": randint(18, 36),
        "height_in": (randint(56, 78)),
        "weight_lbs": randint(90, 300),
        "total_matches": randint(0, 200),
        "total_matches_msgd": randint(0, 100),
        "avg_matches_per_month": randint(0, 50),
        "total_swipes": randint(0, 500),
        "avg_swipes_per_month": randint(0, 100),
        "total_likes": randint(0, 1000),
        "avg_likes_per_month": randint(0, 100),
        "total_time_online_hrs": randint(0, 1000),
        "avg_hrs_per_month": randint(0, 50),
        "total_messages": randint(0, 2000),
        "avg_messages_per_month": randint(0, 100),
        "pic_count": randint(4, 11),
        "bio_word_count": randint(0, 500),
        "days_btwn_last_like": randint(0, 365),
        "days_time_btwn_last_swipe": randint(0, 365),
        "days_btwn_last_match": randint(0, 365),
        "days_btwn_last_online": randint(0, 365),
        "days_btwn_last_message": randint(0, 365)
    }
