"""
이분 그래프
2 초	256 MB

문제
그래프의 정점의 집합을 둘로 분할하여, =>  node를 2개로 분할.
각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,  => 각 node 끼리는 인접하지 않게.
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 
이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 
첫째 줄에 테스트 케이스의 개수 K가 주어진다. 
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 
간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 
각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 

이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 
아니면 NO를 순서대로 출력한다.

제한
2 ≤ K ≤ 5
1 ≤ V ≤ 20,000
1 ≤ E ≤ 200,000
예제 입력 1 
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
예제 출력 1 
YES
NO
예제 입력 2
1
6 7
1 5
1 2
2 6
6 4
5 3
5 6
3 4
에제 출력 2
YES
출처
문제를 번역한 사람: author5
데이터를 추가한 사람: djm03178, doju, eldpswp99
문제의 오타를 찾은 사람: godmoon00
"""
from collections import deque
import sys
input = sys.stdin.readline

is_bipartite = True

def main():
    K = int(input().rstrip()) # 2 ≤ K ≤ 5

    def BFS(first):
            global is_bipartite
            q = deque([(first, 0)])
            visited_odd = [False]*(V+1)
            visited_even = [False]*(V+1)
            visited_even[first] = True
            visited_all[first] = True
            while q:
                start, distance = q.pop()
                
                for next in graph[start]:
                    if (distance+1) % 2 == 0:
                        if visited_odd[next]:
                            q.clear() # while문 끝내기 위함.
                            is_bipartite = False
                            break

                        if not visited_even[next]:
                            q.appendleft((next, distance+1))
                            visited_even[next] = True
                            visited_all[next] = True

                    else:
                        if visited_even[next]:
                            q.clear() # while문 끝내기 위함.
                            is_bipartite = False 
                            break
                        
                        if not visited_odd[next]:
                            q.appendleft((next, distance+1))
                            visited_odd[next] = True
                            visited_all[next] = True
                    
    for _ in range(K):
        V, E = map(int, input().rstrip().split(" ")) # 1 ≤ V ≤ 20,000, 1 ≤ E ≤ 200,000
        graph = [[] for _ in range(V+1)]

        for _ in range(E):
            a, b = map(int, input().rstrip().split(" "))
            graph[a].append(b)
            graph[b].append(a)

        visited_all = [False]*(V+1)
        global is_bipartite

        for node_idx in range(1, V+1):
            if not graph[node_idx]:
                continue
            if not visited_all[node_idx]:
                BFS(node_idx)
            if not is_bipartite:
                break

        if is_bipartite:
            print("YES")
        else:
            print("NO")
            is_bipartite = True


if __name__ == '__main__':
    main()

## 2. 이 외에도 다양한 방법이 있음. ex)color로 마킹 등...





