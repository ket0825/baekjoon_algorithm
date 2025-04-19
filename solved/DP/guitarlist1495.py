"""
기타리스트
시간 제한	메모리 제한
2 초	128 MB
문제
Day Of Mourning의 기타리스트 강토는 다가오는 공연에서 연주할 N개의 곡을 연주하고 있다. 지금까지 공연과는 다른 공연을 보여주기 위해서 이번 공연에서는 매번 곡이 시작하기 전에 볼륨을 바꾸고 연주하려고 한다.

먼저, 공연이 시작하기 전에 각각의 곡이 시작하기 전에 바꿀 수 있는 볼륨의 리스트를 만들었다.
이 리스트를 V라고 했을 때, V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨을 의미한다.
항상 리스트에 적힌 차이로만 볼륨을 바꿀 수 있다. 
즉, 현재 볼륨이 P이고 지금 i번째 곡을 연주하기 전이라면, 
i번 곡은 P+V[i]나 P-V[i] 로 연주해야 한다. 
하지만, 0보다 작은 값으로 볼륨을 바꾸거나, M보다 큰 값으로 볼륨을 바꿀 수 없다.

곡의 개수 N과 시작 볼륨 S, 그리고 M이 주어졌을 때, 
마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하는 프로그램을 작성하시오. 
모든 곡은 리스트에 적힌 순서대로 연주해야 한다.

입력
첫째 줄에 N, S, M이 주어진다. (1 ≤ N ≤ 50, 1 ≤ M ≤ 1,000, 0 ≤ S ≤ M) 
둘째 줄에는 각 곡이 시작하기 전에 줄 수 있는 볼륨의 차이가 주어진다. 
이 값은 1보다 크거나 같고, M보다 작거나 같다.

출력
첫째 줄에 가능한 마지막 곡의 볼륨 중 최댓값을 출력한다. 
만약 마지막 곡을 연주할 수 없다면 (중간에 볼륨 조절을 할 수 없다면) -1을 출력한다.

예제 입력 1 
3 5 10
5 3 7

# 현재 5
차이 5 줄 수 있음.
0 or 10 (0<= <=10)
10.
# 현재 10
차이 3 가능.
7 or 13.
# 현재 7
차이 7 가능

예제 출력 1 
10
예제 입력 2 
4 8 20
15 2 9 10
예제 출력 2 
-1
예제 입력 3 
14 40 243
74 39 127 95 63 140 99 96 154 18 137 162 14 88
예제 출력 3 
238
"""

# 소리 목표값이 정해진 것이 아니라 마지막 곡 볼륨 최댓값 구하는 것임.

import sys
input = sys.stdin.readline

def sol(N, S, M, V):
    visited = [[False] * (M+1) for _ in range(N+1)]
    visited[0][S] = True
    
    debug = False
    # O(N * M)
    possible = False
    for i in range(1, N+1):
        possible = False
        for j in range(M+1):
            if visited[i-1][j]: # 이전 state에 존재했던 값이라면.
                if 0 <= j + V[i-1] <= M: # 이전 state에 볼륨 더한 것
                    visited[i][j + V[i-1]] = True
                    possible = True
                if 0 <= j - V[i-1] <= M: # 이전 state에 볼륨 뺀 것
                    visited[i][j - V[i-1]] = True
                    possible = True
        if debug:
            print(visited[i])
                
        if not possible:
            break
    
    if not possible:
        print(-1)
        return
    else:
        for col in range(M, -1, -1):
            if visited[N][col]:
                print(col)
                break
                 

if __name__ == '__main__':
    N, S, M = map(int, input().strip().split())
    V = list(map(int, input().strip().split()))
    sol(N, S, M, V)


"""
t_case

# 최소만 고르다가 마지막 한 번
4 3 13
1 1 1 13

13

# 부분적 state에서 최대
4 3 13
1 4 2 5

13
"""