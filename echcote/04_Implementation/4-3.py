data = input()
x = ord(data[0])-96
y = int(data[1])

directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
count = 0

for dir in directions:
    new_x = x + dir[0]
    new_y = y + dir[1]

    if new_x > 0 and new_x < 9 and new_y > 0 and new_y < 9:
        count += 1

print(count)