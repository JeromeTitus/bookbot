def get_num_words(string):
    words = string.split()
    num_words = len(words)
    return num_words

def get_num_chars(string):
    word_count = dict()
    for s in string:
        s = s.lower()
        if s in word_count:
            word_count[s] += 1
        else:
            word_count[s] = 1
    return word_count

def sort_dict(d):
    l = list()
    for k in d:
        l.append({k: d[k]})
    l.sort(key=f, reverse=True)
    return l

def f(d):
    for k,v in d.items():
        return v
    
    