"""
약속
시간 제한	메모리 제한
2 초	128 MB
문제
마법사 N명이 머글 문화를 이해하기 위해 머글과 약속을 잡았다. 각 마법사는 한 명의 머글을 만날 예정이다. 하지만, 마법사는 약속 시간보다 빨리 또는 늦게 도착할 수 있기 때문에 고민에 빠졌다. 결국 기다리는 시간을 최소화 하기 위해 모든 약속 시간을 T씩 미루려고 한다. 기다리는 시간은 먼저 도착한 사람이 늦게 도착한 사람이 도착할 때까지 기다리는 시간을 의미한다.

마법사의 약속 시간은 A1, A2, ..., AN이고, 도착 시간은 B1, B2, ..., BN이다. 약속 시간을 T만큼 미루면, 기다리는 시간의 합은 |Ai + T - Bi|의 합과 같다. 기다리는 시간의 합이 최소가 되는 서로 다른 정수 T의 개수를 구해보자.

입력
첫째 줄에 N이 주어진다. 다음 N개의 줄에 Ai, Bi가 주어진다.

출력
첫째 줄에 기다리는 시간의 합이 최소인 서로 다른 정수 T의 개수를 출력한다.

제한
1 ≤ N ≤ 50
1 ≤ Ai, Bi ≤ 109
예제 입력 1 
1
10 9
예제 출력 1 
1
T = -1

예제 입력 2 
2
20 18
30 25
예제 출력 2 
4
T = -5, -4, -3, -2

예제 입력 3 
2
10 11
20 17
예제 출력 3 
5
T = -3, -2, -1, 0, 1

예제 입력 4 
3
10 13
20 15
30 34
예제 출력 4 
1
예제 입력 5 
4
10 14
20 24
30 39
40 37
예제 출력 5 
1
"""

import sys

input = sys.stdin.readline
sys.stdin.write()

def sol():    
    # N명의 약속시간: A. 도착시간: B.
    # 약속 시간을 T만큼 미루기. (모두 미룸)
    # 기다리는 시간의 합이 최소가 되는 정수 개수 T. (음수 가능)
    # sum(A_i + T - B_i)        
    N = int(input().strip()) # 1 ≤ N ≤ 50    
    T = []
    for i in range(N):        
        a, b = map(int, input().strip().split()) # 1 ≤ Ai, Bi ≤ 109                
        t = b - a
        T.append(t)        
        # 단순하게 하면 그 사이 모든 값을 다 하면... 근데 10**9이므로 X.
        # b - a가 더 심플함.        
    # 모두 다 이상적 t값을 찍어보며 확인해보기.
    
    # 그냥 가장 낮은 값을 구하고, 갱신해나가자.        
    min_val = 50 * 1000000000
    final_min_idx1 = 0
    final_min_idx1_val = 0
    final_min_idx2 = -1
    final_min_idx2_val = -1
    for t in range(N):
        cur = 0
        for i in range(N):
            cur += abs(T[t] - T[i])
        if min_val > cur: # 최솟값 갱신
            min_val = cur
            final_min_idx1 = t
            final_min_idx1_val = cur
        elif min_val == cur:
            final_min_idx2 = t      
            final_min_idx2_val = cur                              
    # print("final_min_idx1", final_min_idx1)
    # print("final_min_idx2", final_min_idx2)    
    # print("final_min_idx1_val", final_min_idx1_val)
    # print("final_min_idx2_val", final_min_idx2_val)
    if final_min_idx1_val != final_min_idx2_val:
        print(1)
    else:
        print(abs(T[final_min_idx1] - T[final_min_idx2]) + 1)
                                                        
    
if __name__ == '__main__':
    sol()

# test case
"""
1
1 1000000000

1

1
1000000000 1

1

2 
1000000000 1
1 1000000000

1999999999

4
10 10
20 20
30 30
40 40

1

5
10 12
12 10
10 12
12 10
12 10

1

3
2 4
2 5
2 7

1

4
2 4
2 5
2 7
2 7

3

4
2 7
2 7
2 4
2 5

3

5
2 4
2 4
2 5
2 7
2 7

1

"""