"""
문제
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로
computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고,
도시들 사이에는 길이 있다.(길이 없을 수도 있다)

이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 
다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 
단, 한 번 갔던 도시로는 다시 갈 수 없다. 
(맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 

이런 여행 경로는 여러 가지가 있을 수 있는데, 
가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다.
W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 
비용은 대칭적이지 않다. 
즉, W[i][j] 는 W[j][i]와 다를 수 있다. 
모든 도시간의 비용은 양의 정수이다. 
W[i][i]는 항상 0이다. 
경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 
이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 
가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10) 
다음 N개의 줄에는 비용 행렬이 주어진다. 
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 
갈 수 없는 경우는 0이 주어진다. 
W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.

예제 입력 1 
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0

예제 출력 1 
35
"""
## 1. 내 코드
import sys
input = sys.stdin.readline
min_cost = 1e8  # 10,000,000
"""
4 
0 1 2 3
0 0 2 3
1 0 0 1
0 0 2 0
4
"""
# def main():
#     N = int(input().rstrip("\n")) # (2 ≤ N ≤ 10)
#     # N = 10
#     cost_table = [list(map(int,input().rstrip("\n").split(" "))) for _ in range(N)] # each elem: 1 <= X <= 1,000,000
#     visited = [False]*N
    
#     def dfs(stack:list, cost:int):
#         # if all(visited):
#         if len(stack) == N:
#             if cost_table[stack[-1]][stack[0]] == 0:
#                 return
#             global min_cost
#             cost += cost_table[stack[-1]][stack[0]] # 다시 돌아오는 비용.
#             min_cost = min(min_cost, cost)

#         for i in range(N):
#             if not visited[i] and cost_table[stack[-1]][i] != 0: # stack[-1]은 최근에 방문한 곳.
#                 visited[i] = True
#                 dfs(stack+[i], cost + cost_table[stack[-1]][i])
#                 visited[i] = False                    
                
                
#     for i in range(N):
#         visited[i] = True
#         dfs([i], 0)
#         visited[i] = False

#     print(min_cost)

# if __name__ == '__main__':
#     main()

# ## 2. 다른 점 파악하기.
# import sys
# input = sys.stdin.readline

# final_dist_arr = []

# def dfs_recur(graph, visited, n, node, depth, curr_dist):
# 	if depth == n and graph[node][0] > 0:
# 		final_dist_arr.append(curr_dist + graph[node][0])
# 		return 

# 	for neighbor in range(n):
# 		if (not visited[neighbor] and graph[node][neighbor]):
# 			visited[neighbor] = True
# 			dfs_recur(graph, visited, n, neighbor, depth + 1, curr_dist + graph[node][neighbor])
# 			visited[neighbor] = False

# n = int(input().strip())

# graph = []
# for _ in range(n):
# 	graph.append(list(map(int, input().strip().split(' '))))

# visited = [True] + [False for _ in range(n-1)]
# dist = []


# dfs_recur(graph, visited, n, 0, 1, 0)
# print(min(final_dist_arr))

## 3. 모르겠음 => 어차피 0이니까 처음에 visit을 걸 세팅 안해줘도 되네.
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(2000)
# def dfs(st,now,cnt,total):
#     global Min
#     if total > Min:
#         return
    
#     if cnt == n and st == now:
 
#         Min = min(Min,total)
#         return
#     for i in range(n):
#         if visited[i] == 0 and costs[now][i] != 0:
#             visited[i] = 1
#             # lst.append([now,i,costs[now][i]])
#             dfs(st,i,cnt +1,total + costs[now][i])
#             visited[i] = 0
#             # lst.pop()


# n = int(input())
# costs = [list(map(int,input().split())) for _ in range(n)]
# graph = [[] for _ in range(n)]
# lst = []
# visited = [0] * n
# Min = int(12e9)

# for i in range(n):
#     dfs(i,i,0,0)

# print(Min)


## 4. 내 코드 (VERSION UP) # 2268 -> 160ms
import sys
input = sys.stdin.readline
min_cost = 1e8  # 10,000,000
"""
test case:
4 
0 1 2 3
0 0 2 3
1 0 0 1
0 0 2 0
7

4
0 1 1 1
1 0 1 1
1 1 0 1
1 1 1 0
4
"""
def main():
    N = int(input().rstrip("\n")) # (2 ≤ N ≤ 10)
    # N = 10
    cost_table = [list(map(int,input().rstrip("\n").split(" "))) for _ in range(N)] # each elem: 1 <= X <= 1,000,000
    visited = [False]*N
    tracking_list = []
    cost_list = []
    def dfs(depth:int, N:int, start_node:int, cur_node:int, cost:int):
        global min_cost
        if min_cost < cost: # early pruning
            return

        if depth == N and cost_table[cur_node][start_node] > 0:
            min_cost = min(min_cost, cost + cost_table[cur_node][start_node])
            # tracking_list.append((cur_node, tracking_list[0][0]))
            # cost_list.append(cost_table[cur_node][0])
            # print(tracking_list)
            # print(cost_list)
            # cost_list.pop()
            # tracking_list.pop() 
            return

        for next_node in range(N):
            if not visited[next_node] and cost_table[cur_node][next_node] > 0: # stack[-1]은 최근에 방문한 곳.
                visited[next_node] = True
                # cost_list.append(cost_table[cur_node][next_node])
                # tracking_list.append((cur_node, next_node))
                dfs(depth=depth+1, N=N, start_node=start_node, cur_node=next_node, cost=cost + cost_table[cur_node][next_node])
                visited[next_node] = False
                # cost_list.pop()
                # tracking_list.pop()                    
                                
    for start_node in range(N):
        visited[start_node] = True
        dfs(1, N, start_node, start_node, 0)
        visited[start_node] = False

    print(min_cost)

if __name__ == '__main__':
    main()

## 5. visited를 하나 더 늘려서 진행함. route를 확인.
# import sys
# input = sys.stdin.readline
# MAX = 10_000_000

# def recur(cur, tot):
#     global min_weight
#     if tot >= min_weight:  # Early Pruning
#         return
#     if cur == n:
#         if w[route[cur-1]][0] == 0:  # No path back to start
#             return
#         min_weight = min(min_weight, tot + w[route[cur-1]][0])
#         return

#     for city in range(1, n):
#         cur_weight = w[route[cur-1]][city]
#         if not visited[city] and cur_weight != 0:
#             route[cur] = city
#             visited[city] = True
#             recur(cur + 1, tot + cur_weight)
#             visited[city] = False


# if __name__ == "__main__":
#     n = int(input().strip())
#     w = [list(map(int, input().split())) for _ in range(n)]
#     visited = [False] * n
#     route = [-1] * (n+1)
#     route[0] = 0
#     min_weight = MAX
#     recur(1, 0)
#     print(min_weight)