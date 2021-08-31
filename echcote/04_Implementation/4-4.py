n, m = map(int, input().split())
x, y, dir = map(int, input().split())

# 캐릭터가 방문한 위치 저장
visit = [[0]*m for i in range(n)]
visit[x][y] = 1   # 현재 있는 위치 visit에 저장

game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 1

# 캐릭터가 회전한 횟수
turn = 0

while True:
    # 캐릭터의 방향을 반시계 방향으로 회전
    dir = dir -1 if dir > 0 else 3

    # 캐릭터의 방향으로 한 칸 전진
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 가본 적 없으면서 땅이면 캐릭터 방향으로 전진
    if visit[nx][ny] == 0 and game_map[nx][ny] == 0:
        x = nx
        y = ny

        visit[nx][ny] = 1
        count += 1
        turn = 0
        continue
    # 가본 적 있거나 바다면 회전
    else:
        turn += 1
    
    # 네 방향 모두 다 갈 수 없을 때
    if turn == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        # 뒤가 육지라면 후진
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        # 바다라면 끝!
        else:
            break

        turn = 0
        
print(count)