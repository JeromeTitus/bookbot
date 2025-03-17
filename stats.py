def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> int:
    char_dict = dict()
    for char in text:
        c = char.lower()
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_dict(d: dict) -> list:
    return [{k:v} for k,v in sorted(d.items(), key=lambda x: x[1], reverse=True) if k.isalpha()]