from collections import defaultdict
import random


def extract_words():
    with open('/usr/share/dict/american-english', 'r') as f:
        raw_data = f.read().split('\n')
        data = filter(is_clean, raw_data)
        return data


def is_clean(word):
    if "'" in word:
        return False
    if len(word) != 9:
        return False
    if '\\x' in word:
        return False
    if word.lower() != word:
        return False
    return True


def extract_cores(wordlist):
    coremap = defaultdict(list)
    for word in wordlist:
        coremap[word[3:6]].append(word)
    return coremap


all_words = extract_words()
coremap = extract_cores(all_words)


class Wordmonger(object):

    def __init__(self, all_words, coremap):
        self.words = all_words
        self.coremap = coremap

    def answer_count(self, candidate):
        value = self.coremap.get(candidate, None)
        if value is None:
            return 0
        else:
            return value

    def answers(self, candidate):
        return self.coremap.get(candidate, None)

    def generate(self):
        key = random.choice(self.coremap.keys())
        return key
        # return self.coremap[key]

    def check(self, arg):
        return arg in self.coremap[arg[3:6]]


monger = Wordmonger(all_words, coremap)
