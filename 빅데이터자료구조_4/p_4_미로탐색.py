from collections import deque

def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:  # 범위 바깥
        return False
    elif map[y][x] == '1' or map[y][x] == '.':  # 벽이거나 이미 방문한 위치
        return False
    return True

def BFS():
    que = deque()
    que.append((0, 1))
    print('BFS: ')
    

    while que:
        here = que.popleft()
        print(here, end='->')
        x, y = here
        if (map[y][x] == 'x') : return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1) : que.append((x, y - 1))
            if isValidPos(x, y + 1) : que.append((x, y + 1))
            if isValidPos(x - 1, y) : que.append((x - 1, y))
            if isValidPos(x + 1, y) : que.append((x + 1, y))
    return False

            
map = [ ['1', '1', '1', '1', '1', '1' ],
        ['e', '0', '1', '0', '0', '1' ],
        ['1', '0', '0', '0', '1', '1' ],
        ['1', '0', '1', '0', '1', '1' ],
        ['1', '0', '1', '0', '0', 'x' ],
        ['1', '1', '1', '1', '1', '1' ]  
]
MAZE_SIZE = 6
result = BFS()
if result : print('--> 미로탐색 성공')
else : print('--> 미로탐색 실패')