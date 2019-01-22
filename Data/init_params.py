# Boolean Cluster - Non depend on another
def gen_bool_tup():
    return ("username_possibly_offensive", "white", "black", "hispanic",
            "asian", "native_american", "pacific_islander", "other_race",
            "smoker", "drinker", "interested_in_men", "interested_in_women",
            "intested_in_hookup", "intested_in_casual",
            "intested_in_short_term", "intested_in_long_term", "likes_sports",
            "likes_reading", "likes_games", "likes_food", "likes_tv",
            "has_full_body_pic", "has_friends_pic", "has_cat_pic",
            "has_dog_pic", "has_risque_pic", "has_hobby_1_pic",
            "has_hobby_2_pic", "has_hobby_3_pic", "has_closed_reopened_acct")


# Categorical Cluster - One hot: Only one from a subset
def gen_cat_dict():
    return {
        "sex": ("M", "F"),
        "state":
        ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
         "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA",
         "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY",
         "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX",
         "UT", "VT", "VA", "WA", "WV", "WI", "WY"),
        "personality_test_1": ("I", "E"),
        "personality_test_2": ("S", "N"),
        "personality_test_3": ("F", "T"),
        "personality_test_4": ("J", "P"),
        "subscr_status": ("Free", "Paid"),
        "job_title": ("Doctor", "Lawyer", "Engineer", "Manager",
                      "Social Worker", "Teacher", "Politician", "Musician",
                      "Bartender", "Pet Counselor"),
        "education": ("High School", "Some College", "Bachelors", "Masters",
                      "Doctorate"),
        "major": ("STEM", "Arts", "Music", "Business", "Law", "Social Science",
                  "Philosophy", "Psychology", "Language", "Education",
                  "History"),
        "minor": ("STEM", "Arts", "Music", "Business", "Law", "Social Science",
                  "Philosophy", "Psychology", "Language", "Education",
                  "History"),
        "religious_views": ("Christian", "Jewish", "Muslim", "Hindu",
                            "Buddhist", "Agnostic", "Atheist"),
        "political_views": ("Democrat", "Republican", "Constitution",
                            "Independent", "Green", "Socialist", "Libertarian")
    }


# List Cluster - Can include 0 or more
def gen_list_dict():
    return {
        "languages": ("English", "Spanish", "German", "French", "Other"),
        "skills": ("Programming", "Public Speaking", "Microsoft Office", "CPR",
                   "Art", "Writing", "Leadership", "Social Media"),
        "sports":
        ("Eagles", "Ravens", "Steelers", "Cardinals", "Saints", "Falcons",
         "Panthers", "Bears", "Cowboys", "Packers", "Colts"),
        "foods": ("Sushi", "Steak", "Pie", "Ice Cream", "Quinoa", "Indian",
                  "Mexican", "Italian"),
        "movies": ("Shawshank", "The Godfather", "Star Wars", "Titanic",
                   "Waterboy", "Spirited Away", "Pulp Fiction",
                   "Schindlers List"),
        "music": ("Rock", "Metal", "Jazz", "Country", "Rap", "Classical",
                  "Country"),
        "games": ("Shooters", "Board", "Card", "RPG", "Puzzle", "Platformer"),
        "quotes": ("Einstein", "Oscar Wilde", "Bible", "Bob Dylan",
                   "Wizard of Oz")
    }
