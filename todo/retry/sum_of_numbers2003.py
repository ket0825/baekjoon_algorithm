"""
수들의 합 2
시간 제한	메모리 제한
0.5 초	128 MB
문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다.

예제 입력 1 
4 2
1 1 1 1
예제 출력 1 
3
예제 입력 2 
10 5
1 2 3 4 2 5 3 1 1 2
예제 출력 2 
3

t_case
10 5
1 2 3 4 2 6 3 1 1 2

2
----
1 1
10

0
----
1 10
1

0
---
1 1
1

1
----
3 5
1 1 1

0
----
5 3
1 3 5 7 9

1
----
4 2
3 3 3 3

0
---
4 7
3 4 4 3

2
"""

import sys

input = sys.stdin.readline

# 이것도 가능
def sol2(N, M, A):    
    cnt = 0
    start = 0
    end = 1
    acc_sum = A[0]
    # 마지막에서 줄어드는 로직을 구현하지 않음.
    while end < N:
        print(f"start: {start}, end: {end}")
        if acc_sum < M:
            acc_sum+=A[end]
            end+=1
        elif acc_sum == M:
            acc_sum+=A[end]
            end+=1
            acc_sum-=A[start]
            start+=1
            cnt+=1
        elif acc_sum > M:
            acc_sum-=A[start]
            start+=1            
    
    # 마지막 부분 체크 필요    
    while start < N and acc_sum >= M:
        if acc_sum == M:
            cnt+=1
            break
        else:
            acc_sum-=A[start]
            start+=1                
        
    return cnt
    
            

def sol(N, M, A):     
    cnt = 0    
    start = 0
    end = 0
    acc_sum = 0
    
    while start < N:
        if acc_sum < M and end < N: # end가 N 도달하지 않음.
            acc_sum+=A[end]
            end+=1
        elif acc_sum == M:
            cnt+=1            
            acc_sum-=A[start]
            start+=1
        elif acc_sum > M or end == N:
            acc_sum-=A[start]
            start+=1
        
    return cnt

if __name__ == '__main__':    
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    cnt = sol(N, M, A)
    cnt = sol2(N, M, A)
    print(cnt)