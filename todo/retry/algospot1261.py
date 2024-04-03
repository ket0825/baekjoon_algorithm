"""
알고스팟
1 초 (추가 시간 없음)	128 MB
문제
알고스팟 운영진이 모두 미로에 갇혔다. 
미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 
미로는 빈 방 또는 벽으로 이루어져 있고, 
빈 방은 자유롭게 다닐 수 있지만, 
벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 
즉, 여러 명이 다른 방에 있을 수는 없다. 
어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 
즉, 현재 운영진이 (x, y)에 있을 때, 
이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1)이다. 
단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 
알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 
빈 방과 동일한 방으로 변한다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 
벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 
세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다. 
다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 
0은 빈 방을 의미하고, 1은 벽을 의미한다.

(1, 1)과 (N, M)은 항상 뚫려있다.

출력
첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 
벽을 최소 몇 개 부수어야 하는지 출력한다.

예제 입력 1 
3 3
011
111
110
예제 출력 1 
3
예제 입력 2 
4 2
0001
1000
예제 출력 2 
0
예제 입력 3 
6 6
001111
010000
001111
110001
011010
100010
예제 출력 3 
2
"""

# 간 곳 마킹 + 뚫은 곳 count...
# 최소 거리가 아닌 최소 뚫기임.
# 1. BFS... 그러나 전역 탐색 및 중복 탐색. 10000개.
import sys
from collections import deque
input = sys.stdin.readline

def main():
    M, N = map(int, input().rstrip().split(" ")) # (1 ≤ N, M ≤ 100)
    graph = [list(map(int, input().rstrip())) for _ in range(N)]

    graph_count = [[0]*M for _ in range(N)]
    visited = [[False]* M for _ in range(N)]
    dx_list = [-1, 1, 0, 0]
    dy_list = [0, 0, -1, 1]
    visited[0][0] = True
    q = deque()
    q.appendleft((0,0))

    while q:
        x, y = q.pop()

        for dx, dy in zip(dx_list, dy_list):
            if not (0 <= x + dx < N and 0 <= y + dy < M):
                continue
            print(f"x+dx:{x+dx}, y+dy: {y+dy}")

            # 방문했었으면
            if visited[x+dx][y+dy]:
                # 방문했었는데 그래프가 0이라면 (벽이 아니라면)
                if graph[x+dx][y+dy] == 0:
                    # 그리고 graph_count가 더 적은 상태라면
                    if graph_count[x][y] < graph_count[x+dx][y+dy]:
                        graph_count[x+dx][y+dy] = graph_count[x][y]
                        q.appendleft((x+dx, y+dy))            
                # 방문했었는데 그래프가 0이 아니라면 (벽이라면)
                else:
                    if graph_count[x][y]+1 < graph_count[x+dx][y+dy]:
                        graph_count[x+dx][y+dy] = graph_count[x][y] + 1
                        q.appendleft((x+dx, y+dy))            
            else:
                visited[x+dx][y+dy] = True
                q.appendleft((x+dx,y+dy))
                if graph[x+dx][y+dy] == 0:                    
                    graph_count[x+dx][y+dy] = graph_count[x][y]        
                else: # 처음 마주한 벽인 경우.
                    graph_count[x+dx][y+dy] = graph_count[x][y] + 1
                    
            
    print(graph_count[N-1][M-1])


if __name__ == '__main__':
    main()
    
## 2. heapq 사용: 출처: ghtjd6908	
"""
이 문제는 최단 경로 문제의 변형으로, 
BFS(Breadth-First Search) 알고리즘을 활용하여 해결할 수 있습니다. 

다만 일반적인 BFS와 달리, 
벽을 부수는 비용을 최소화해야 하므로 
heapq 모듈을 사용하여 우선순위 큐를 구현합니다.
heapq를 사용하는 과정은 다음과 같습니다:

시작점 (0, 0)에서 도착점 (m-1, n-1)까지 가는 경로를 찾습니다.
큐에는 (벽을 부순 개수, 현재 좌표) 형태의 튜플을 저장합니다.
큐에서 요소를 꺼낼 때, 벽을 부순 개수가 작은 순서대로 꺼냅니다. 
즉, 최소 비용 경로를 우선적으로 탐색합니다.
"""
import sys
from heapq import heappop, heappush
# heapq는 최소 priority queue임.
# 만약 heapq에 들어가는 원소가 여러 개면, 앞에 있는 것이 작을수록 순서가 앞쪽임.

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]

visit = [[0] * n for _ in range(m)]
q = []      # 벽 부신 개수, 좌표
heappush(q, (0, 0, 0))
while q:
    res, x, y = heappop(q)
    if x == m - 1 and y == n - 1:
        print(res)
        exit(0)
    visit[x][y] = 1
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if nx in range(m) and ny in range(n):
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                if arr[nx][ny] == '0':
                    heappush(q, (res, nx, ny))
                else:
                    heappush(q, (res + 1, nx, ny))

