"""
지름길
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	14797	8638	6547	58.623%
문제
매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다. 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

입력
첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.

출력
세준이가 운전해야하는 거리의 최솟값을 출력하시오.

예제 입력 1 
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90
예제 출력 1 
70
예제 입력 2 
2 100
10 60 40
50 90 20
예제 출력 2 
80
예제 입력 3 
8 900
0 10 9
20 60 45
80 190 100
50 70 15
160 180 14
140 160 14
420 901 5
450 900 0
예제 출력 3 
432

3 100
0 1 99
0 90 10
1 89 1

3 100
1 101 1
40 90 1
10 50 1

"""

import sys
input = sys.stdin.readline

def sol():
    N, D = map(int, input().strip().split()) # N <= 12, 1 <= D <= 10000. (자연수)
    shortcuts = [
        list(map(int, input().strip().split())) for _ in range(N)
    ] # 시작 위치, 도착 위치, 지름길 길이.    
    # 하나하나 갈 때 마다 최소 거리인 거 확인
    # 길 하나하나 걸을 때마다 N 확인 -> O(max(N) * max(D)) => 120000.
    # 도착위치 기준 정렬이 되면 더 최적화 가능.
    shortcuts.sort(key=lambda x: (x[1], x[2]))
    
    dp = [0] * (D+1) # init
    shortcut_idx = 0
    for i in range(1, D+1):
        dp[i] = dp[i-1]+1
        while shortcut_idx < N and shortcuts[shortcut_idx][1] == i:
            entry = shortcuts[shortcut_idx][0]
            shortcut_dist = shortcuts[shortcut_idx][2]
            # print(f"현재 거리: {i}")
            # print("지름길 진입 전:", dp[i])
            dp[i] = min(dp[i], dp[entry] + shortcut_dist)
            # print("지름길 진입 후:", dp[i])
            shortcut_idx+=1
            # print(f"shortcut_idx: {shortcut_idx}")        
    
    print(dp[D])


if __name__ == '__main__':
    sol()