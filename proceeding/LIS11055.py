"""
가장 큰 증가하는 부분 수열
1 초	256 MB
문제
수열 A가 주어졌을 때, 
그 수열의 증가하는 부분 수열 중에서 
합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 
수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 
합이 가장 큰 증가하는 부분 수열은 A = {1, 2, 50, 60} 이고, 합은 113이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 합이 가장 큰 증가하는 부분 수열의 합을 출력한다.

예제 입력 1 
10
1 100 2 50 60 3 5 6 7 8
예제 출력 1 
113

예제 입력 2
8
9 8 7 6 1 2 3 4
예제 출력 2
10

출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: gee308, gomyk12, mohana9
"""

## 1. N^2 algorithm. 
# 수열의 i번째 것이 j번째 보다 크다면, 
# i번째 dp와 j번째 dp에 수열에 j번째를 더한 것 중 
# 더 큰 것을 i번째 dp에 재할당한다.

import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip()) # (1 ≤ N ≤ 1,000)
    S = [0] + list(map(int, input().rstrip().split(" "))) # (1 ≤ Ai ≤ 1,000)
    dp = S[:]
    
    for i in range(1, N+1):
        for j in range(1, i):
            if S[i] > S[j]:
              dp[i] = max(dp[i], dp[j] + S[i])
    
    print(max(dp))
                

if  __name__ == '__main__':
    main()

## 2. nlogn algorithm... after.
