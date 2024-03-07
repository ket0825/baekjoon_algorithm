"""
1, 2, 3 더하기 3

문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 
합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, 
n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 1,000,000보다 작거나 같다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 
1,000,000,009로 나눈 나머지를 출력한다.

예제 입력 1 
3
4
7
10
예제 출력 1 
7
44
274
출처
문제를 만든 사람: baekjoon
어색한 표현을 찾은 사람: game9777
"""
##1. dp problem
import sys
input = sys.stdin.readline

def main():
    T = int(input().rstrip('\n'))
    N_cases = [int(input().rstrip('\n')) for _ in range(T)]
    max_case = max(N_cases)
    dp = [0] * (max_case+1 if max_case > 4 else 4)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if max_case > 3:
        for i in range(4, max_case+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009

    for n in N_cases:
        print(dp[n])


if __name__ =='__main__':
    main()
