"""
트리
시간 제한	메모리 제한
2 초	128 MB

문제
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

예를 들어, 다음과 같은 트리가 있다고 하자.


현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.


이제 리프 노드의 개수는 1개이다.

입력
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

출력
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

예제 입력 1 
5
-1 0 0 1 1
2
예제 출력 1 
2
예제 입력 2 
5
-1 0 0 1 1
1
예제 출력 2 
1
예제 입력 3 
5
-1 0 0 1 1
0
예제 출력 3 
0
예제 입력 4 
9
-1 0 0 2 2 4 4 6 6
4
예제 출력 4 
2
---
6
-1 0 0 2 2 2
2

1
---
6
-1 0 0 2 2 2
1

3
---
4
-1 0 1 2
2

1
"""

import sys
input = sys.stdin.readline        

def sol():
    N = int(input().strip()) # 1 <= N <= 50
    tree = list(map(int, input().strip().split()))
    # tree.sort() # 순서 변경 염두.
    remove_idx = int(input().strip()) # 0 <= N <= 49
    # 아니면 graph로 나타낼까.    
    graph = [[] for _ in range(N)]
    for i in range(N):
        if tree[i] == -1:
            continue
        graph[tree[i]].append(i)
    # print(graph)
    
    stack = [remove_idx]
    while stack:
        next_idx = stack.pop()
        # print(f"현재 노드: {next_idx}")
        if graph[next_idx]:
            for nx in range(len(graph[next_idx])):
                stack.append(graph[next_idx][nx])
                graph[next_idx][nx] = -1
        else:
            graph[next_idx].append(-1) # -1은 삭제한 것임.
    
    # print(graph)    
    leaf = 0
    for node in graph:
        if not node: # 삭제된 노드는 -1로 채워짐
            leaf+=1
        # 부모가 remove_idx 하나만 자식으로 가진 경우, 부모도 leaf_node가 됨.
        elif len(node) == 1 and node[0] == remove_idx:
            leaf+=1
                            
    print(leaf)       


if __name__ == '__main__':
    sol()