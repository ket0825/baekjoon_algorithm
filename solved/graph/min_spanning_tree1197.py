"""
최소 스패닝 트리
시간 제한	메모리 제한	
1 초	128 MB
문제
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

예제 입력 1 
3 3
1 2 1
2 3 2
1 3 3
예제 출력 1 
3

"""

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

def add_edges(edges, node, visited, graph):    
    for next_node, weight in graph[node].items():
        if not visited[next_node]: # 이미 방문했던 것 제외.
            heapq.heappush(edges, (weight, next_node))
    # print(f"추가된 노드: {node}, 갱신된 edges: {edges} ")        

def prim(V, E):
    graph = defaultdict(dict)
    visited = [False] * (V+1)
    
    for _ in range(E):
        a, b, w = map(int, input().strip().split())
        if graph.get(a):
            graph[a][b] = min(graph[a].get(b, 1000001), w)
            graph[b][a] = min(graph[b].get(a, 1000001), w)
        else:
            graph[a][b] = w # 중복되는 edge 존재함!
            graph[b][a] = w

    
    # 1부터 시작.
       
    edges = [(v, k) for k, v in graph[1].items()]
    visited[1] = True
    heapq.heapify(edges)
    # print(edges)    
    total = 0    
    visited_count = 1
    
    while edges and visited_count < V: # edges 유무까지 확인
        w, end = heapq.heappop(edges)                                    
        if visited[end]: # 방문한 경우.
            continue                                       
        visited_count+=1
        visited[end] = True
        # print(f"현재 가중치: {w}")
        total+=w
        # 갈 수 있는 edge 갱신
        add_edges(edges, end, visited, graph)
        
    print(total)        

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

class DisjointSet:
    
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
    
    def find(self, x):        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # DFS와 같이 끝까지 내려가서, 결과가 연속적으로 루트 값으로 할당된다.            
        
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # 높이가 같으면 이어붙임.
            self.parent[root_y] = root_x
            self.rank[root_x]+=1
    
    def is_same_set(self, x, y):
        return self.find(x) == self.find(y)
        

def kruskal(V, E):
    edges = []
    for _ in range(E):
        a, b, weight = map(int, input().strip().split())
        if a < b:            
            edges.append((weight, a, b))
        else:
            edges.append((weight, b, a))
    
    edges.sort(key=lambda x: x[0], reverse=True)
    ds = DisjointSet(V)
    # print(f"edges: {edges}")
    total = 0
    edge_cnt = 0
    while edge_cnt < V-1:
        w, start, end = edges.pop()
        # print(f"서로소 집합 parent 확인: {ds.parent}")
        # 싸이클 확인을 위하여 disjoint set 활용.
        if not ds.is_same_set(start, end):            
            edge_cnt+=1
            total+=w
            ds.union(start, end)
    
    # print(f"서로소 집합 parent 확인: {ds.parent}")
    print(total)
        

if __name__ == '__main__':
    V, E = map(int, input().strip().split())
    kruskal(V, E)
    # prim(V, E)
    
"""
t_case

# 갱신 여부 확인
6 9
1 2 5
1 3 7
2 3 1
2 4 2
3 4 3
3 5 4
4 5 5
4 6 9
5 6 8

20

# 음수 가중치 
6 9
1 2 5
1 3 7
2 3 -19
2 4 2
3 4 3
3 5 4
4 5 5
4 6 9
5 6 8

0

# 노드 2개, edge 1개.
2 1
1 2 5

5

# 음수 가중치
2 1
1 2 -1

-1

# 음수 최대
2 1
1 2 -2147483648

-2147483648

# 성형 구조
6 10
1 2 10
1 5 10
1 6 1
2 6 1
3 6 1
6 4 1
5 6 1
2 4 10
3 5 10
4 1 10

5

# 중복 엣지
6 9
1 2 4
1 2 5
2 1 3
4 5 2
1 2 1
2 1 6
3 4 2
2 3 2
5 6 2

9
 
"""