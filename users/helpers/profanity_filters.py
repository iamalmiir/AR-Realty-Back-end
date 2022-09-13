from better_profanity import profanity

profanity.load_censor_words_from_file("users/helpers/profanity_words.txt")


def profanity_filter(data):
    for credential in data.values():
        if profanity.contains_profanity(credential):
            raise ValueError("Profanity is not allowed.")
