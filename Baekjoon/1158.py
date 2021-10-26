# 7, 3
# 1, 2, 3, 4, 5, 6, 7
# 3
# 1, 2, ^, 4, 5, 6, 7
# 6
# 1, 2, 4, 5, ^, 7
# 2
# 1, ^, 4, 5, 7
# 7
# 1, 4, 5, ^
# 5
# 1, 4, ^
# 1
# ^, 4
# 4

n, k = map(int, input().split())

josephus = []
l = [x+1 for x in range(n)]
index = 0
while True:
    index = (index + k - 1 ) % len(l)
    josephus.append((l.pop(index)))
    if not l:
        break
    
print('<'+', '.join(map(str, josephus))+'>')