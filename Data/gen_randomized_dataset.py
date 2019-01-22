from numpy.random import randint
from random import choice, sample
"""
The dataset will be organized into various
clusters with clear biases.  The outline is provided below:

Cluster 1 - Older, White, Christian, & Republican

Cluster 2 - Younger, Mixed, Agnostic, & Democrat

Cluster 3 - Doctorate, STEM, Doctor/Lawyer/Engineer

Cluster 4 - Heavy, Atheist, Libertarian

Cluster 5 - Short, Asian, Educated, Shy

Cluster 6 - Muslim/Buddhist/Hindu, Pacific Islander/Other, Long Term

Cluster 7 - Homosexual

Cluster 8 - Bisexual

Cluster 9 - More Matches - Females

Cluster 10 - More Matches - Males
"""


# Boolean Features
def return_bool_cluster(bool_keys):
    bool_vect = randint(0, 2, len(bool_keys))
    return dict(zip(bool_keys, bool_vect))


# Categorical Features
# def return_cat_cluster():
#     return {
#         "sex":
#         choice(("M", "F")),
#         "personality_test_1":
#         choice(("I", "E")),
#         "personality_test_2":
#         choice(("S", "N")),
#         "personality_test_3":
#         choice(("F", "T")),
#         "personality_test_4":
#         choice(("J", "P")),
#         "subscr_status":
#         choice(("Free", "Paid")),
#         "job_title":
#         choice(("Doctor", "Lawyer", "Engineer", "Manager", "Social Worker",
#                 "Teacher", "Politician", "Musician", "Bartender",
#                 "Pet Counselor")),
#         "education":
#         choice(("High School", "Some College", "Bachelors", "Masters",
#                 "Doctorate")),
#         "major":
#         choice(("STEM", "Liberal Arts", "Music", "Nursing", "Business", "Law",
#                 "Sociology", "Humanities", "Philosophy", "Psychology",
#                 "Language")),
#         "minor":
#         choice(("STEM", "Liberal Arts", "Music", "Nursing", "Business", "Law",
#                 "Sociology", "Humanities", "Philosophy", "Psychology",
#                 "Language")),
#         "religious_views":
#         choice(("Christian", "Jewish", "Muslim", "Hindu", "Buddhist",
#                 "Agnostic", "Atheist")),
#         "political_views":
#         choice(("Democrat", "Republican", "Constitution", "Independent",
#                 "Green", "Socialist", "Libertarian"))
#     }

# Date Features
# def return_date_cluster():
#     return {
#         "join_date": 0,
#         "last_like_time": 0,
#         "last_swipe_time": 0,
#         "last_match_time": 0,
#         "last_online_time": 0,
#         "last_message_time": 0,
#         "time_btwn_last_like": 0,
#         "time_btwn_last_swipe": 0,
#         "time_btwn_last_match": 0,
#         "time_btwn_last_online": 0,
#         "time_btwn_last_message": 0
#     }


# List Features
def return_list_cluster(languages, skills, sports, food, movies, music, games,
                        quotes):
    return {
        "languages_spoken": sample(languages, randint(0, len(languages))),
        "skills": sample(skills, randint(0, len(skills))),
        "fav_foods_keywds": sample(food, randint(0, len(food))),
        "fav_sports_teams_keywds": sample(sports, randint(0, len(sports))),
        "fav_movies_keywds": sample(movies, randint(0, len(movies))),
        "fav_music_keywds": sample(music, randint(0, len(music))),
        "fav_games_keywds": sample(games, randint(0, len(games))),
        "fav_quote_keywds": sample(quotes, randint(0, len(quotes)))
    }


# Ordinal Features
# def return_ord_cluster():
#     return {
#         "id": randint(1000000, 9999999),
#         "age": randint(18, 36),
#         "height": (randint(5, 6), randint(0, 11)),
#         "weight": randint(90, 300),
#         "location": 0,
#         "total_matches": randint(0, 200),
#         "avg_matches_per_month": randint(0, 50),
#         "total_swipes": randint(0, 500),
#         "avg_swipes_per_month": randint(0, 100),
#         "total_likes": randint(0, 1000),
#         "avg_likes_per_month": randint(0, 100),
#         "total_time_online_hrs": randint(0, 1000),
#         "avg_hrs_per_month": randint(0, 50),
#         "total_messages": randint(0, 2000),
#         "avg_messages_per_month": randint(0, 100),
#         "pic_count": randint(4, 11),
#         "bio_word_count": randint(0, 500)
#     }
"""
# Random Data
"""
# Bool Cluster
bool_keys = ("username_possibly_offensive", "white", "black", "hispanic",
             "asian", "native_american", "pacific_islander", "other_race",
             "smoker", "drinker", "interested_in_men", "interested_in_women",
             "intested_in_hookup", "intested_in_casual",
             "intested_in_short_term", "intested_in_long_term", "likes_sports",
             "likes_reading", "likes_games", "likes_food", "likes_tv",
             "has_full_body_pic", "has_friends_pic", "has_cat_pic",
             "has_dog_pic", "has_risque_pic", "has_hobby_1_pic",
             "has_hobby_2_pic", "has_hobby_3_pic", "has_closed_reopened_acct")
bool_dict = return_bool_cluster(bool_keys)

# List Cluster
languages = ("English", "Spanish", "German", "French", "Other")
skills = ("Programming", "Public Speaking", "Microsoft Office", "CPR", "Art",
          "Writing", "Leadership", "Social Media")
sports = ("Eagles", "Ravens", "Steelers", "Cardinals", "Saints", "Falcons",
          "Panthers", "Bears", "Cowboys", "Packers", "Colts")
food = ("Sushi", "Steak", "Pie", "Ice Cream", "Quinoa", "Indian", "Mexican",
        "Italian")
movies = ("Shawshank", "The Godfather", "Star Wars", "Titanic", "Waterboy",
          "Spirited Away", "Pulp Fiction", "Schindlers List")
music = ("Rock", "Metal", "Jazz", "Country", "Rap", "Classical", "Country")
games = ("Shooters", "Board", "Card", "RPG", "Puzzle", "Platformer")
quotes = ("Einstein", "Oscar Wilde", "Bible", "Bob Dylan", "Wizard of Oz")
list_dict = return_list_cluster(languages, skills, sports, food, movies, music,
                                games, quotes)
