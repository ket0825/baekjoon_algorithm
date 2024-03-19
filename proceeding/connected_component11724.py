"""
연결 요소의 개수
3 초	512 MB
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
(1 ≤ u, v ≤ N, u ≠ v) 
같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
예제 입력 2 
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2 
1
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: djm03178, seoo2001, YunGoon
잘못된 조건을 찾은 사람: songjuh
"""

## 1. search graph by BFS.
import sys
input = sys.stdin.readline
from collections import deque

def main():
    N, M = map(int, input().rstrip().split(" "))    # (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
    graph = [[] for _ in range(N+1)]

    for i in range(M):
        u, v = map(int,input().rstrip().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (N+1)
    
    def BFS(start):
        q = deque([start])

        while q:
            start = q.pop()

            for elem in graph[start]:
                if not visited[elem]:
                    visited[elem] = True
                    q.appendleft(elem)


    count = 0
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            BFS(i)
            count +=1

    print(count)


if __name__ == '__main__':
    main()


## 2. queue를 사용하지 않고, 마킹하면서 바로 진행.
import sys

def solve(v):
    visited[v] = 1
    for i in range(len(g[v])):
        if not visited[g[v][i]]:
            solve(g[v][i])


N, M = map(int, sys.stdin.readline().split())
g = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
# print(g)
group = 0
for i in range(1, N+1):
    if not visited[i]:
        solve(i)
        group += 1
print(group)