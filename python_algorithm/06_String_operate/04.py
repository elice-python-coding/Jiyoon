'''가장 흔한 단어'''
import re
import collections

def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]