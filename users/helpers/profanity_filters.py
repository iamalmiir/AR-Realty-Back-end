from better_profanity import profanity

profanity.load_censor_words_from_file("users/helpers/profanity_words.txt")


def register_data_filter(data):
    credentials = [data["full_name"], data["email"], data["username"]]
    for item in data_to_filer:
        if profanity.contains_profanity(item):
            raise ValueError("Profanity is not allowed.")
