"""
미로 탐색
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	192 MB	196306	89476	56866	44.025%
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9
예제 입력 3 
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3 
38
예제 입력 4 
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4 
13
출처
데이터를 추가한 사람: djm03178, jh05013, poia0304, sait2000
"""
## 1. 최소이니 DFS보단 BFS가 더 빠름. (어차피 완전탐색)
from collections import deque
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().rstrip().split(" ")) # N, M(2 ≤ N, M ≤ 100)
    graph = [list(map(int, input().rstrip())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    def BFS(start_node: tuple):
        q = deque()
        q.appendleft(start_node)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        
        while q:
            x, y, count =  q.pop()

            if x == N-1 and y == M-1: # early pruning.
                return count

            for k in range(4):
                next_x = x + dx[k]
                next_y = y + dy[k]
                if (0 <= next_x < N 
                    and 0 <= next_y < M 
                    and graph[next_x][next_y] == 1
                    and not visited[next_x][next_y]
                    ):
                    visited[next_x][next_y] = True
                    q.appendleft((next_x, next_y, count+1))

    visited[0][0] = True
    print(BFS((0,0,1)))


if __name__ == '__main__':
    main()


## 2. count를 안하고, 원본 그래프에 그려가며 바로 진행해도 된다. 출처: ckh214

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))  # readline의 경우 맨 뒤에 '\n'까지 입력받으므로 제거해줘야 함

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


print(bfs(0, 0))