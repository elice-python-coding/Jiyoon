'''https://www.acmicpc.net/problem/1181'''

import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)