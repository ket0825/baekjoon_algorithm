"""
정수 삼각형
2 초	128 MB
문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 

아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 
또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 
삼각형을 이루고 있는 각 수는 모두 정수이며, 
범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 
둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

예제 입력 1 
5
7   
3 8 
8 1 0 
2 7 4 4 
4 5 2 6 5
예제 출력 1 
30
출처
Olympiad > International Olympiad in Informatics > IOI 1994 > Day 1 1번

Olympiad > USA Computing Olympiad > 2005-2006 Season > USACO December 2005 Contest > Bronze ?번

Olympiad > USA Computing Olympiad > 1999-2000 Season > USACO Fall 1999 Contest > Gold 1번

문제의 오타를 찾은 사람: apjw6112, Martian, paranocean
잘못된 조건을 찾은 사람: djm03178
데이터를 추가한 사람: eunhyekim1223, hwangtmdals
잘못된 데이터를 찾은 사람: thanatos0128
"""

## 1. dp에 input으로 받은 요소들을 더해나가기. N(N+1)/2
import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip('\n'))
    dp = [0] * (N+1)
    dp[1] = [int(input().rstrip('\n'))]

    if N > 1:
        for n in range(2,N+1):
            depth = list(map(int, input().rstrip().split(" ")))
            dp[n] = [0]*(n)
            dp[n][0] = dp[n-1][0] + depth[0] # 맨 처음 부분.
            dp[n][n-1] = dp[n-1][n-2] + depth[n-1] # 맨 마지막 부분.

            for i in range(1, n-1): # 그 외 부분.
                dp[n][i] = max(dp[n-1][i-1], dp[n-1][i]) + depth[i]

    print(max(dp[N]))


if __name__ == '__main__':
    main()


## 2. 뒤에서부터 더해나가는 방식. 출처: gjh020717
import sys

input = sys.stdin.readline

size = int(input().rstrip())

triangle = [list(map(int, input().split())) for _ in range(size)]
D = [[0] * i for i in range(1, size+1)]
for i in range(size):
    D[size-1][i] = triangle[size-1][i]


for i in range(size-2, -1, -1):
    for j in range(0, i+1):
        D[i][j] = triangle[i][j] + max(D[i+1][j], D[i+1][j+1])

print(D[0][0])
