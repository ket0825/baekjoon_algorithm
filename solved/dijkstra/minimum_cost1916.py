"""
최소비용 구하기
시간 제한	메모리 제한
0.5 초	128 MB
문제
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

입력
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

예제 입력 1 
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
예제 출력 1 
4

7
11
1 2 4
1 3 6
1 6 12
2 3 1
2 4 2
3 5 2
4 5 6
4 6 3
4 7 5
5 7 4
6 7 1
1 7

10
"""

import sys
import heapq
input = sys.stdin.readline


def dijkstra(start, end):
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        cost, node = heapq.heappop(pq)
        if distances[node] < cost:
            continue
        # print(f"cost: {cost}, node: {node}")
        for v_node, v_cost in graph[node]:
            # print(f"{node} -> {v_node}, 기존 비용: {distances[v_node]}, 갱신 시도 비용: {cost + v_cost} ")
            if distances[v_node] > cost + v_cost:
                distances[v_node] = cost + v_cost
                heapq.heappush(pq, (cost + v_cost, v_node))

    return distances[end]
        

if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, cost = map(int, input().strip().split())
        graph[a].append((b, cost))
    
    distances = [float('inf')] * (N+1)
    start, end = map(int, input().strip().split())
    
    print(dijkstra(start, end))
    






















# import heapq
# import sys
# sys.setrecursionlimit(10000000)

# input = sys.stdin.readline

# def dijkstra(start, end, graph, distance):
#     distance[start] = 0
#     min_heap = [(0, start)]
        
#     while min_heap:
#         cur_cost, cur_node = heapq.heappop(min_heap)
#         # print(f"distance: {distance}")
        
#         if distance[cur_node] < cur_cost: # 방문했는데 비용이 더 크다면?
#             continue  # 비용이 같은 것은 넘기는 이유가 바로 전에 갱신했던 값이 들어오기 때문! 
        
#         for next_node, next_weight in graph[cur_node]:
#             if next_weight + cur_cost < distance[next_node]:
#                 distance[next_node] = next_weight + cur_cost
#                 heapq.heappush(min_heap, (next_weight + cur_cost, next_node))
    
#     return distance[end]
            

# if __name__ == '__main__':
#     N = int(input().strip())
#     M = int(input().strip())
#     graph = [[] for _ in range(N+1)]
#     for _ in range(M):
#         a, b, weight = map(int, input().strip().split())
#         graph[a].append((b, weight))
        
#     start, end = map(int, input().strip().split())
#     distance = [float('inf')] * (N+1)
#     answer = dijkstra(start, end, graph, distance)
#     print(answer)
    