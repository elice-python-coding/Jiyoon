from collections import itertools
from string import ascii_lowercase

def getPermutation(n, r):

    perm = itertools.permutations(ascii_lowercase[:n], r)
    result = []
    for dt in perm:
        result.append(''.join(dt))

    return result