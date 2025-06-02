"""
특정 거리의 도시 찾기
시간 제한	메모리 제한
2 초	256 MB
문제
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.



이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.  2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

입력
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

출력
X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

예제 입력 1 
4 4 2 1
1 2
1 3
2 3
2 4
예제 출력 1 
4
예제 입력 2 
4 3 2 1
1 2
1 3
1 4
예제 출력 2 
-1
예제 입력 3 
4 4 1 1
1 2
1 3
2 3
2 4
예제 출력 3 
2
3

6 6 2 1
1 2
1 3
2 4
3 4
4 5
4 6

4

6 6 3 1
1 2
1 3
2 4
3 4
4 5
4 6

5
6
---
7 6 3 7
1 2
1 3
2 4
3 4
4 5
4 6

-1
---
6 6 4 1
1 2
1 3
2 4
3 4
4 5
4 6

-1
"""

import sys
import heapq
input = sys.stdin.readline

def dijkstra(min_heap, K, graph, distance):
    answers = []
    while min_heap:
        # print("현재 heap:", min_heap)
        # print(f"거리: {distance}")
        cur_dist, cur_node = heapq.heappop(min_heap)
        if distance[cur_node] < cur_dist: # 최소 거리 우선으로 방문한 것이기에 이미 방문함 것임
            continue
        
        for next_node, weight in graph[cur_node]:
            if weight + cur_dist < distance[next_node]:
                distance[next_node] = weight + cur_dist # weight는 1임.
                # print(f"next_node: {next_node}, next_dist: {weight + cur_dist}")
                if K == distance[next_node]:
                    answers.append(next_node) # 종료
                else:
                    heapq.heappush(min_heap, (weight + cur_dist, next_node))
    # print(distance)
    return answers


if __name__ == '__main__':
    N, M, K, X = map(int, input().strip().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().strip().split())
        w = 1
        graph[u].append((v, w))
        
    distance = [float('inf')] * (N+1)
    min_heap = [(0, X)]      
    distance[X] = 0
    answers = dijkstra(min_heap, K, graph, distance)
    if answers:
        answers.sort()
        print(*answers, sep='\n')
    else:
        print(-1)
        
# BFS도 가능!