"""
숨바꼭질 3
2 초	512 MB
문제
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 

수빈이는 걷거나 순간이동을 할 수 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 
1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 
몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. 
N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
2
힌트
수빈이가 5-10-9-18-17 순으로 가면 2초만에 동생을 찾을 수 있다.

출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: eric00513, idiot, mohana9, tagun11, ulight
"""

"""
BFS로 풀면 이미 방문한 것이 최적으로 가는 방향이라는 가정이 반드시 필요함!
푸는 방법 3가지: 출처: djm03178
1. 다익스트라 알고리즘
2. 0-1 BFS: 가중치가 0인 간선에 연결된 정점은 큐의 맨 뒤가 아닌 맨 앞에 넣는 방법
3. *2를 별도의 간선으로 생각하지 않고, +1이나 -1에 의한 좌표를 큐에 넣을 때 
그 좌표의 2의 거듭제곱 배인 좌표들을 전부 큐에 넣는 방법
"""

## 1. BFS
# T cases: https://forward-gradually.tistory.com/70

import sys
from collections import deque

input = sys.stdin.readline

def main():
    # N K를 input(Num)
    N, K = map(int, input().rstrip().split(" "))
    # 만약 수빈이가 동생보다 앞에 있으면, 무조건 차이가 답.    
    if N >= K:
        print(N-K)
        return
    # location[1000001] 생성. max_num으로.
    location = [-1] * 100001
    # q 생성 및 수빈이 위치와 count를 체크.
    # 수빈이 위치를 location에 0으로.
    q = deque([N])
    location[N] = 0
    # 기본에서의 제곱수들은 모두 0으로 초기화.
    t = 2*N
    while 0 < t <= 100000:
        location[t] = 0
        q.appendleft(t)
        t*=2

    while location[K] == -1:
        start = q.pop()

        # 100000보다 작고, start+1이 방문하지 않았다면
        if start+1 <= 100000 and location[start+1] == -1:
            t = start+1
            # 제곱을 거듭하면서 모두 location에 기록하고, q에 넣음.
            while t <= 100000:
                if location[t] == -1:
                    location[t] = location[start]+1
                    q.appendleft(t)
                t*=2
        # 0보다 크고, start-1이 방문하지 않았다면.
        if start - 1 >= 0 and location[start-1] == -1:
            t = start-1
            # 제곱을 거듭하면서 모두 location에 기록하고, q에 넣음.
            while 0 < t <= 100000:
                if location[t] == -1:
                    location[t] = location[start]+1
                    q.appendleft(t)
                t*=2

    print(location[K])

    
if __name__ == "__main__":
    main()

