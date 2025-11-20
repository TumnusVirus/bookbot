# from pydoc import text


def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(counts):
    return counts["num"]

def chars_dict_to_sorted_list(counts):
#sorted_dict={}
    sorted_list = []
    for ch in counts:
        sorted_dict = {"char":ch, "num": counts[ch]}
        sorted_list.append(sorted_dict)
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list