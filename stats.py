def get_num_words(text):
    t = text.split()
    return len(t)

def get_word_count(text):
    word_count = dict()
    for letter in text:
        w = letter.lower()
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    return word_count

def sort_dict(d):
    l = []
    for k, v in d.items():
        l.append(
            {
                "char": k,
                "count": v
            }
        )
    return sorted(l, key=lambda x: x["count"], reverse=True)


    
