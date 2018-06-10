import sys
import json


def is_better(language_level, dictionary):
    language, level = language_level
    _, current_top_level = dictionary[language]
    return level > current_top_level


def update_result(language_level, first_name, last_name, result):
    language, _ = language_level
    del result[language]
    return add_to_result(language_level, first_name, last_name, result)


def add_to_result(language_level, first_name, last_name, result):
    full_name = "{} {}".format(first_name, last_name)
    language, level = language_level
    result[language] = (full_name, level)
    return result


def top_coding_skill(dictionary):
    result = {}
    people_skills = dictionary["people"]

    for human in people_skills:
        languages_levels = [(x["name"], x["level"]) for x in human["skills"]]
        for language_level in languages_levels:
            language = language_level[0]
            if language in result.keys():
                if is_better(language_level, result):
                    result = update_result(language_level,
                                           human["first_name"],
                                           human["last_name"],
                                           result)
            else:
                result = add_to_result(language_level,
                                       human["first_name"],
                                       human["last_name"],
                                       result)

    return result


def print_result(result):
    for x, y in result.items():
        print("{} - {}".format(x, y[0]))


def main():
    with open(sys.argv[1]) as f:
        dictionary = json.load(f)
        result = top_coding_skill(dictionary)
        print_result(result)


if __name__ == '__main__':
    main()
