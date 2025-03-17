import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = args[-1]
    print(f"Analyzing book found at {filepath}")

    txt = get_book_text(filepath=filepath)
    word_count = count_words(txt)
    print("---------- Word Count -----------")
    print(f'Found {word_count} total words')

    char_count = count_characters(txt)
    print("------- Character Count ---------")
    char_list = sort_dict(char_count)
    for c in char_list:
        for k,v in c.items():
            print(f'{k}: {v}')
    print("--------- END --------")

main()
