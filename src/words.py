from collections import defaultdict, OrderedDict
import random
from pprint import pprint


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
        self.challenge = OrderedDict()

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

    def show_challenge(self):
        pprint(self.challenge)

    def formulate_challenge(self, n=10):
        self.challenge = OrderedDict()
        while n > 0:
            new_core = random.choice(self.coremap.keys())
            if new_core not in self.challenge.keys():
                self.challenge[new_core] = None
                n -= 1

    def claim(self, answer):
        key = answer[3:6]
        if (
            answer in self.coremap[key]
            and key in self.challenge.keys()
        ):
            self.challenge[key] = answer
            return True
        else:
            return False


monger = Wordmonger(all_words, coremap)
