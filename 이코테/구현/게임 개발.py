n, m = map(int, input().split())

# 방문 위치 저장
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

# 맵 정보
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 행 북 0 남 2
dx = [-1, 0, 1, 0]
# 열 동 1 서 3
dy = [0, 1, 0, -1]

def turn_left():
    global direction # 바깥에서 선언된 전역변수이기 때문에
    direction -= 1 # 왼쪽으로 돌기
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        # 뒤에 보고
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 갈 수 있다면 가기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)