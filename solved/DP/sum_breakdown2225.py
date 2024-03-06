"""
합분해 S(n, k) 인듯. 집합의 분할이었음.

문제
0부터 N까지의 정수 K개를 더해서 
그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 
또한 한 개의 수를 여러 번 쓸 수도 있다.

입력
첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

출력
첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1 
20 2
예제 출력 1 
21
예제 입력 2 
6 4
예제 출력 2 
84
출처
잘못된 데이터를 찾은 사람: tncks0121
"""

## 1. 공식이 유도되었음. 집합의 분할 문제였음.
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().rstrip('\n').split(" ")) # N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)
    # 0 20, 20 0은 다른 것이고, 되기도 함.
    
    # N K = N K-1, N-1 K-1, ... , 0 K-1.
    # N K-1 = N K-2, N-1 K-2, ...

    dp = [[1 for _ in range(N+1)]  for _ in range(K+1) ] # dp[K][N]
    # dp[1][1] => 1 1에 대한 경우의 수임.
    # dp[1][2] => 2 1에 대한 경우의 수임.
    # dp[2][3] => dp[1][3] + dp[1][2] + dp[1][1] + dp[1][0] => 
    
    for i in range(N+1):
        dp[0][i] = 0 # K가 0이면 0.

    for k in range(2,K+1):
        for n in range(1,N+1):
             dp[k][n] = (dp[k][n-1] + dp[k-1][n])%1000000000

    
    print(dp[K][N]%1000000000)


if __name__ == '__main__':
    main()


## 2. 어차피 더해주면서 가기 때문에 공식이 유도되지 않아도 저장하면서 가면 됨.
# import sys
# n, k = map(int, sys.stdin.readline().split())

# dp = [[0] * (n+1) for _ in range(k+1)]

# for i in range(n+1):
#     dp[1][i] = 1

# for i in range(2, k+1):
#     s = 0
#     for j in range(n+1):
#         s += dp[i-1][j]
#         dp[i][j] = s

# print(dp[k][n]%1000000000)