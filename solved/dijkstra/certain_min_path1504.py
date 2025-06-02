"""특정한 최단 경로
시간 제한	메모리 제한
1 초	256 MB
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.

예제 입력 1 
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
예제 출력 1 
7

---
8 11
1 2 3
1 3 2
2 4 3
2 6 5
4 3 5
6 4 1
4 5 4
5 8 15
6 7 1
5 7 9
8 7 1
5 6

17

"""
import sys
import heapq

input = sys.stdin.readline
# 두 정점 중 우선 순위는 상관없음
# 1 -> u -> v -> N
# 1 -> v -> u -> N
#  u -> v는 공통
# 현재 5번 했는데, 3번만 해도 가능!

def dijkstra(start, end, N, graph):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    # print(f"{start} -> {end}")
    min_heap = [(0, start)]
    while min_heap:
        cur_cost, cur_node = heapq.heappop(min_heap)
        # print("distance", distance)
        if distance[cur_node] < cur_cost:
            continue
        
        for next_node, weight in graph[cur_node]:
            if cur_cost + weight < distance[next_node]:
                distance[next_node] = cur_cost + weight
                heapq.heappush(min_heap, (cur_cost + weight, next_node))
    
    # print(distance[end])
    return distance[end]


if __name__ == '__main__':
    N, E = map(int, input().strip().split())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(E):
        a, b, c = map(int, input().strip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    u, v = map(int, input().strip().split())    
    uv_dist = dijkstra(u, v, N, graph)
    shortest = min(dijkstra(1, v, N, graph) + dijkstra(u, N, N, graph), dijkstra(1, u, N, graph) + dijkstra(v, N, N, graph))    
    answer = uv_dist + shortest
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)


""" 출처: spawn1215er. 더욱 최적화 가능!

import sys, heapq

input = sys.stdin.readline

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

n ,e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
dist_from_start = dijkstra(1, graph, n)
dist_from_v1 = dijkstra(v1, graph, n)
dist_from_v2 = dijkstra(v2, graph, n)
result = min(
    dist_from_start[v1] + dist_from_v1[v2] + dist_from_v2[n],
    dist_from_start[v2] + dist_from_v2[v1] + dist_from_v1[n]
)
if result == float('inf'):
    print(-1)
else:
    print(result)
"""
    

