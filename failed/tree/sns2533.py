"""
사회망 서비스(SNS)
시간 제한	메모리 제한
3 초	256 MB
문제
페이스북, 트위터, 카카오톡과 같은 사회망 서비스(SNS)가 널리 사용됨에 따라, 사회망을 통하여 사람들이 어떻게 새로운 아이디어를 받아들이게 되는가를 이해하는 문제가 중요해졌다. 사회망에서 사람들의 친구 관계는 그래프로 표현할 수 있는데,  이 그래프에서 사람은 정점으로 표현되고, 두 정점을 잇는 에지는 두 정점으로 표현되는 두 사람이 서로 친구 관계임을 표현한다. 

예를 들어, 철수와 영희, 철수와 만수, 영희와 순희가 서로 친구 관계라면 이를 표현하는 친구 관계 그래프는 다음과 같다. 



친구 관계 그래프를 이용하면 사회망 서비스에서 어떤 새로운 아이디어가 전파되는 과정을 이해하는데 도움을 줄 수 있다. 어떤 새로운 아이디어를 먼저 받아들인 사람을 얼리 아답터(early adaptor)라고 하는데, 사회망 서비스에 속한 사람들은 얼리 아답터이거나 얼리 아답터가 아니다. 얼리 아답터가 아닌 사람들은 자신의 모든 친구들이 얼리 아답터일 때만 이 아이디어를 받아들인다. 

어떤 아이디어를 사회망 서비스에서 퍼뜨리고자 할 때, 가능한 한 최소의 수의 얼리 아답터를 확보하여 모든 사람이 이 아이디어를 받아들이게 하는  문제는 매우 중요하다. 

일반적인 그래프에서 이 문제를 푸는 것이 매우 어렵다는 것이 알려져 있기 때문에, 친구 관계 그래프가 트리인 경우, 즉 모든 두 정점 사이에 이들을 잇는 경로가 존재하면서 사이클이 존재하지 않는 경우만 고려한다. 

예를 들어, 8명의 사람으로 이루어진 다음 친구 관계 트리를 생각해보자. 2, 3, 4번 노드가 표현하는 사람들이 얼리 아답터라면, 얼리 아답터가 아닌 사람들은 자신의 모든 친구가 얼리 아답터이기 때문에 새로운 아이디어를 받아들인다.



친구 관계 트리가 주어졌을 때, 모든 개인이 새로운 아이디어를 수용하기 위하여 필요한 최소 얼리 어답터의 수를 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 친구 관계 트리의 정점 개수 N이 주어진다. 단, 2 ≤ N ≤ 1,000,000이며, 각 정점은 1부터 N까지 일련번호로 표현된다. 두 번째 줄부터 N-1개의 줄에는 각 줄마다 친구 관계 트리의 에지 (u, v)를 나타내는 두 정수 u와 v가 하나의 빈칸을 사이에 두고 주어진다. 

출력
주어진 친구 관계 그래프에서 아이디어를 전파하는데 필요한 얼리 아답터의 최소 수를 하나의 정수로 출력한다.

예제 입력 1 
8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
예제 출력 1 
3
예제 입력 2 
9
1 2
1 3
2 4
3 5
3 6
4 7
4 8
4 9
예제 출력 2 
3
---
6
1 2
1 3
3 4
4 5
4 6

2
---
11
1 2
1 3
1 4
2 5
2 6
2 7
3 8
4 9
8 10
8 11

4
---
5
1 2
2 3
3 4
4 5

2
---
3
1 2
2 3

1
---
5
1 2
1 3
1 4
1 5

1
---
10
1 2
1 3
1 4
4 5
4 6
5 7
5 8
6 9
6 10

3
---
9
1 2
1 3
2 4
3 5
4 6
4 7
5 8
5 9

3
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6 + 100)

# 실패: 상향식 접근 필요! 규칙 기반 하향식은 잘 되지 않음.
# def sol():
#     N = int(input().strip()) # 2 ≤ N ≤ 1,000,000
#     tree = [[] for _ in range(N+1)] # N+1개의 Node.        
#     early_adapters = [False] * (N+1)
#     for _ in range(N-1):
#         a, b = tuple(map(int, input().strip().split()))        
#         tree[a].append(b)
#         tree[b].append(a)
    
#     # print(tree)
    
#     # N이 많으니 recursion 말고, stack으로 dfs 구현.
#     # 루트 노드가 얼리어답터 아닐 때,    
#     def find_min_early_adapter():
#         cnt = 0
#         stack = [(0, 1)]            
#         while stack:
#             prev_visit, to_visit = stack.pop()
#             # 한 칸씩 내려가서 확인해야 함.
#             for next in tree[to_visit]:
#                 if next != to_visit: # 동일하면 X
#                     continue
#                 if not tree[next]:
#                     if not early_adapters[to_visit]:
#                         # print(f"리프 노드가 있음! 노드 {to_visit}")
#                         early_adapters[to_visit] = True
#                         cnt+=1
#                 else: # 다음 노드가 있음.
#                     stack.append((to_visit, next))
            
#             # 현재 노드가 얼라이답터가 아니고, 이전 노드도 얼리어답터가 아니라면
#             # 현재 노드 얼리어답터
#             if not early_adapters[to_visit] and not early_adapters[prev_visit]: 
#                 # print(f"더할 게 있는데 이전 노드는 얼리어답터가 아님! {to_visit}")
#                 early_adapters[to_visit] = True
#                 cnt+=1            
                        
#         # print(cnt)
#         # for i in range(1, N+1):
#         #     if early_adapters[i]:
#         #         print(f"얼리어답터: {i}")
#         return cnt
    
#     early_adapters[0] = True # 루트 노드 얼리어답터 아니게 만들기 위함.
#     cnt1 = find_min_early_adapter()
#     early_adapters = [False] * (N+1) # 루트 노드 얼리어답터.
#     cnt2 = find_min_early_adapter()
                    
#     print(min(cnt1, cnt2))

# 트리 아래서부터 올라오며 얼리어답터인게 좋은지 안좋은지 상태를 기록하면서 확인.
def sol():
    N = int(input().strip()) # 2 ≤ N ≤ 1,000,000
    tree = [[] for _ in range(N+1)] # N+1개의 Node.            
    for _ in range(N-1):
        a, b = map(int, input().strip().split())
        tree[a].append(b)    
        tree[b].append(a)
    
    # 0은 현재 노드 얼리어답터 아닌 경우
    # 1은 현재 노드 얼리어답터인 경우
    dp = [[-1, -1] for _ in range(N+1)]
    
    def dfs(node, parent):
        dp[node][0] = 0 # 현재 노드가 얼리어답터 아님.
        dp[node][1] = 1 # 현재 노드가 얼리어답터.
        
        for child in tree[node]:            
            if child != parent:
                dfs(child, node)
                # 노드가 얼리어답터 아니면 child는 반드시 얼리어답터.
                dp[node][0] += dp[child][1]
                # 노드가 얼리어답터 아니면 child는 얼리어답터이거나, 아닌 경우 중 더 작은거.
                dp[node][1] += min(dp[child][0], dp[child][1])
        
    dfs(1, -1)
    
    print(min(dp[1][0], dp[1][1]))    

if __name__ == '__main__':
    sol()