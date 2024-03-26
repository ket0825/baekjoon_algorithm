"""
나이트의 이동
1 초	256 MB
문제
체스판 위에 한 나이트가 놓여져 있다.
나이트가 한 번에 이동할 수 있는 칸은 
아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?


입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l × l이다. 
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 
나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1 
5
28
0
출처
University > Tu-Darmstadt Programming Contest > TUD Contest 2001 3번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: sait2000
문제의 오타를 찾은 사람: sgchoi5
"""
## 1. queue and count with graph.
import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(l, knight_x, knight_y, target_x, target_y):
    board = [[-1 for _ in range(l)] for _ in range(l)]
    q = deque()
    board[knight_x][knight_y] = 0
    q.append((knight_x, knight_y))
    
    while q:
        x, y = q.pop()

        if x == target_x and y == target_y:
            print(board[x][y])
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < l 
                and 0 <= ny < l
                and board[nx][ny] == -1
                ):
                board[nx][ny] = board[x][y] + 1
                q.appendleft((nx, ny))

def main():
    T = int(input().rstrip())

    for _ in range(T):
        l = int(input().rstrip())
        knight_x, knight_y = map(int,input().rstrip().split(" "))
        target_x, target_y = map(int,input().rstrip().split(" "))
        BFS(l, knight_x, knight_y, target_x, target_y)


if __name__ == '__main__':
    main()