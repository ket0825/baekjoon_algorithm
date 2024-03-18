"""
ABCDE

2 초	512 MB
문제
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 
사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 
일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 
A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.

위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 
친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, 
a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 
같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

출력
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

예제 입력 1 
5 4
0 1
1 2
2 3
3 4
예제 출력 1 
1
예제 입력 2 
5 5
0 1
1 2
2 3
3 0
1 4
예제 출력 2 
1
예제 입력 3 
6 5
0 1
0 2
0 3
0 4
0 5
예제 출력 3 
0
예제 입력 4 
8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7
예제 출력 4 
1
출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: forever900, jmkk27, memo, pjh1016
문제의 오타를 찾은 사람: jason9319
"""

##1. graph 그리고 search (BFS). one way가 아님.
import sys
from collections import deque

input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split(" ")) # N (5 ≤ N ≤ 2000), M (1 ≤ M ≤ 2000)
    graph = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().rstrip().split(" ")) # (0 ≤ a, b ≤ N-1, a ≠ b) 
        graph[a].append(b)
        graph[b].append(a)
        
    finished = False
    
    for i in range(N):
        node = graph[i]
        if finished:
            break

        if not node:
            continue

        q = deque()

        for elem in node:
            q.appendleft((elem,[i, elem]))   

        while not finished and q:
            if finished:
                break
            else:
                start, visited = q.pop()
                
                for next in graph[start]:
                    if next not in visited:
                        if len(visited)+1 == 5:
                            # print(visited+[next])
                            finished = True
                            break
                        q.appendleft((next, visited+[next]))

    if finished:
        print(1)
    else:
        print(0)
        
        
if __name__ == '__main__':
    main()


##2. graph 그리고 search (DFS)


