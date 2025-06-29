def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    num_chars = {}
    for char in text:
        char = char.lower()
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sort_on(items):
    return items["num"]

def get_sorted_num_chars(num_chars):
    num_chars_list = []
    for key, val in num_chars.items():
        num_chars_list.append({"char": key, "num": val})
    num_chars_list.sort(reverse=True, key=sort_on)
    return num_chars_list
