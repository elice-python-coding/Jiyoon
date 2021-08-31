'''https://www.acmicpc.net/problem/11279'''
import sys
import heapq

n = int(input())

max_heap = []
for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(max_heap) > 0:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -m)
