from stats import get_num_words, get_num_chars, get_sorted_num_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_stats(filepath):
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    num_chars = get_num_chars(contents)
    sorted_num_chars = get_sorted_num_chars(num_chars)

    return num_words, sorted_num_chars

def print_report(filepath, num_words, num_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in num_chars:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    num_words, num_chars = get_stats(filepath)
    print_report(filepath, num_words, num_chars)

main()
