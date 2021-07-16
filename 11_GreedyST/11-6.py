
food_times = list(map(int, input().split()))
k = int(input())

food_index = 0
length = len(food_times)
count = 0

while count < k:
    if food_times[food_index] > 0:
        food_times[food_index] -= 1
        count += 1
    food_index = (food_index + 1) % length

print(food_index + 1)
