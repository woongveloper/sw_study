from collections import deque

length, width, height = map(int,input().split())
matrix = [[] * width for _ in range(height)]

for z in range(height):
    for y in range(width):
        matrix[z].append(list(map(int,input().split())))

Q = deque()
unripe = 0
ripe = 0
for x in range(length):
    for y in range(width):
        for z in range(height):
            if matrix[z][y][x] == 1:
                Q.append((x,y,z))
                ripe += 1
            elif matrix[z][y][x] == 0:
                unripe += 1

def bfs():
    dif = [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)]
    mx = -1
    now = Q.popleft()
    while True:
        for dir in range(6):
            dx = now[0] + dif[dir][0]
            dy = now[1] + dif[dir][1]
            dz = now[2] + dif[dir][2]
            if 0<=dx<=length-1 and 0<=dy<=width-1 and 0<=dz<=height-1 and matrix[dz][dy][dx] == 0:
                Q.append((dx,dy,dz))
                matrix[dz][dy][dx] = matrix[now[2]][now[1]][now[0]] + 1
                mx = matrix[now[2]][now[1]][now[0]] + 1
        if Q == deque():
            for x in range(length):
                for y in range(width):
                    for z in range(height):
                        if matrix[z][y][x] == 0:
                            return -1
            return mx - 1
        else:
            now = Q.popleft()

if unripe == 0:
    print('0')
elif ripe == 0:
    print('-1')
else:
    print(bfs())