from CircularQueue import CircularQueue


map = [
    ['1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1'],
]


SIZE = 6

def isValidPos(r,c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    return False

def BFS():
    Q = CircularQueue()
    Q.enqueue((1,0))
    print('BFS: ')

    while not Q.isEmpty(): #움직일 공간이 있다면
        pos = Q.dequeue() #움직일 공간을 받아온다.
        #print(pos,end'->')

        print(pos,end= '-> ') #화면에 위치를 찍는다
        (r,c) = pos

        if (map[r][c] == 'x'):
            return True

        else:
            map[r][c] = '.' #방문하지 않도록 다른기호로 표시 해둔다

            if isValidPos(r - 1, c): Q.enqueue((r - 1 , c))
            if isValidPos(r + 1 , c): Q.enqueue((r + 1, c))
            if isValidPos(r, c - 1): Q.enqueue((r, c - 1))
            if isValidPos(r, c + 1): Q.enqueue((r, c + 1))
        print(Q)
    return False

def printMaze(pos): #재미삼아 교수님이 해본대
    r,c = pos

    for i in range(SIZE): # 2차원 배열 찍는 과정임
        for j in range(SIZE):
            if i == r and j == c:
                print(' @ ',end='')
            else:
                print(f' {map[i][j]} ',end='')

        print()
    print()


if __name__ == '__main__':
    result = BFS()

    if result: #true라면
        print("성ㄱㅇ했")
    else:
        print("실패했")
