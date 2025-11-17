def count_words(text):
    return len(text.split())

def count_letters(text):
    letters_dict = {}

    for letter in text:
        if letter.lower() in letters_dict:
            letters_dict[letter.lower()] += 1
        else:
            letters_dict[letter.lower()] = 1

    return letters_dict

def sort_list(list):
    return list["num"]

def generate_list(letters_dict):
    dict_list = []

    for letter in letters_dict:
        letter_count_dict = {"char": letter, "num": letters_dict[letter]}
        dict_list.append(letter_count_dict)

    sorted_list = sorted(dict_list, key=sort_list, reverse=True)
    return sorted_list