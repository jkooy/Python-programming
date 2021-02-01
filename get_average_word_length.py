def get_average_word_length(words):
    '''
    Compute the average length of the words
    '''
    import random
    assert len(words) > 0
    assert isinstance(words, list)
    
    for i in words:
        assert isinstance(i, str)

    length = 0
    for i in words:
        length += len(i)

    return length/len(words)


from urllib.request import urlopen
u='https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
response = urlopen(u)
words = [i.strip().decode('utf8') for i in response.readlines()]
print(get_average_word_length(words))


def get_longest_word(words):
    '''
    What is the longest word (get_longest_word(words))?
    '''
    import random
    assert len(words) > 0
    assert isinstance(words, list)
    
    for i in words:
        assert isinstance(i, str)

    longestw = 0
    longestW = 0
    for w in words:
        if len(w) > longestw:
            longestw = len(w)
            longestW = w
    return longestW
print(get_longest_word(words))


def get_longest_words_startswith(words,start):
    '''
    What is the longest word that starts with a single letter (get_longest_words_startswith(words,start))
    '''
    import random
    assert len(words) > 0
    assert isinstance(words, list)
    assert isinstance(start, str)
    assert len(start) > 0
    assert len(start) == 1
    assert start.isalpha()
    
    for i in words:
        assert isinstance(i, str)


    longestw = 0
    longestW = 0
    for w in words:
        if w[0] == start:
            if len(w) > longestw:
                longestw = len(w)
                longestW = w
    return longestW
print(get_longest_words_startswith(words, 'a'))


def get_most_common_start(words):
    '''
    What is the most common starting letter (get_most_common_start(words))?
    '''
    assert len(words) > 0
    assert isinstance(words, list)

    for i in words:
        assert isinstance(i, str)

    d ={}
    for w in words:
        if w[0] not in d.keys():
            d[w[0]] = 1
        else:
            d[w[0]] += 1
    common = max(d, key = d.get)
    return common
print(get_most_common_start(words))

def get_most_common_end(words):
    '''
    What is the most common starting letter (get_most_common_start(words))?
    '''
    assert len(words) > 0
    assert isinstance(words, list)

    for i in words:
        assert isinstance(i, str)

    d ={}
    for w in words:
        if w[-1] not in d.keys():
            d[w[-1]] = 1
        else:
            d[w[-1]] += 1
    common = max(d, key = d.get)
    return common
print(get_most_common_end(words))