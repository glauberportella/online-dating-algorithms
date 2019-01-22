from numpy.random import random, randint
from random import choice, sample
from time import localtime, mktime, strptime, strftime


# Boolean Cluster - Non depend on another
def return_bool_cluster(bool_tup):
    return dict(zip(bool_tup, randint(0, 2, len(bool_tup))))


# Categorical Cluster - One hot: Only one from a subset
def return_cat_cluster(cat_dict):
    return {
        "sex": choice(cat_dict["sex"]),
        "state": choice(cat_dict["state"]),
        "personality_test_1": choice(cat_dict["personality_test_1"]),
        "personality_test_2": choice(cat_dict["personality_test_2"]),
        "personality_test_3": choice(cat_dict["personality_test_3"]),
        "personality_test_4": choice(cat_dict["personality_test_4"]),
        "subscr_status": choice(cat_dict["subscr_status"]),
        "job_title": choice(cat_dict["job_title"]),
        "education": choice(cat_dict["education"]),
        "major": choice(cat_dict["major"]),
        "minor": choice(cat_dict["minor"]),
        "religious_views": choice(cat_dict["religious_views"]),
        "political_views": choice(cat_dict["political_views"])
    }


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

    return {
        "join_date": join_date,
        "last_like_time": randomDate(join_date, "1/1/2019 12:00 AM", random()),
        "last_swipe_time": randomDate(join_date, "1/1/2019 12:00 AM",
                                      random()),
        "last_match_time": randomDate(join_date, "1/1/2019 12:00 AM",
                                      random()),
        "last_online_time": randomDate(join_date, "1/1/2019 12:00 AM",
                                       random()),
        "last_message_time": randomDate(join_date, "1/1/2019 12:00 AM",
                                        random()),
        "days_btwn_last_like": randint(0, 365),
        "days_time_btwn_last_swipe": randint(0, 365),
        "days_btwn_last_match": randint(0, 365),
        "days_btwn_last_online": randint(0, 365),
        "days_btwn_last_message": randint(0, 365)
    }


# List Cluster - Can include 0 or more
def return_list_cluster(list_dict):
    return {
        "languages":
        sample(list_dict["languages"], randint(0,
                                               len(list_dict["languages"]))),
        "skills":
        sample(list_dict["skills"], randint(0, len(list_dict["skills"]))),
        "sports":
        sample(list_dict["sports"], randint(0, len(list_dict["sports"]))),
        "foods":
        sample(list_dict["foods"], randint(0, len(list_dict["foods"]))),
        "movies":
        sample(list_dict["movies"], randint(0, len(list_dict["movies"]))),
        "music":
        sample(list_dict["music"], randint(0, len(list_dict["music"]))),
        "games":
        sample(list_dict["games"], randint(0, len(list_dict["games"]))),
        "quotes":
        sample(list_dict["quotes"], randint(0, len(list_dict["quotes"])))
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
        "bio_word_count": randint(0, 500)
    }
