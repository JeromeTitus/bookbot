import sys

from stats import get_num_words, get_num_chars,  sort_dict

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = args[1]
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {path}...")
    txt = get_book_text(path)

    num_words = get_num_words(txt)
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")

    word_dict = get_num_chars(txt)
    count_list = sort_dict(word_dict)
    print("---------- Character Count -----------")
    for w in count_list:
        for k in w:
            if k.isalpha():
                print(f"{k}: {w[k]}")  

main()
