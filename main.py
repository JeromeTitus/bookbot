import sys

from stats import get_num_words, get_word_count, sort_dict

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = args[1]
    print("==========BOOKBOT==========")
    txt = get_book_text(path)
    print(f"Analysing book found at {path}")
    num_words = get_num_words(txt)
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    word_count = get_word_count(txt)
    sorted_word_count = sort_dict(word_count)
    print("---------- Character Count ----------")
    for d in sorted_word_count:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["count"]}")



main()