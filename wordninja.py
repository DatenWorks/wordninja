import os
import re
import gzip
import itertools
from math import log


# I did not author this code, only tweaked it from:
# http://stackoverflow.com/a/11642687/2449774
# Thanks Generic Human!


_DEFAULT_LANG = os.getenv("WORDNINJA_LANG") or "en_US"
# Build a cost dictionary
# assuming Zipf's law and cost = -math.log(probability).
with gzip.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'wordninja',
                            _DEFAULT_LANG,
                            'wordninja_words.txt.gz')) as f:
    words = f.read().decode().split()
__LOG_TOTAL = log(len(words))
_wordcost = dict((k, log((i+1)*__LOG_TOTAL)) for i, k in enumerate(words))
_maxword = max(len(x) for x in words)
_SPLIT_RE = {
    'en_US': re.compile("[^a-zA-Z0-9]+"),
    'pt_BR': re.compile("[^a-zA-Z0-9À-ÿ]+")
}


def split(s):
    """Uses dynamic programming to infer the location of
    spaces in a string without spaces."""
    return list(itertools.chain.from_iterable(
        itertools.repeat(item, 1)
        if isinstance(item, str)
        else item for item in map(_split,
                                  _SPLIT_RE.get(_DEFAULT_LANG).split(s))))


def _split(s):
    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-_maxword):i]))
        return min((c + _wordcost.get(s[i-k-1:i], 9e999), k+1)
                   for k, c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1, len(s)+1):
        c, k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i > 0:
        c, k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return reversed(out)
