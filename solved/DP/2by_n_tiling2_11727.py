"""
문제
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×17 직사각형을 채운 한가지 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
2
예제 출력 1 
3
예제 입력 2 
8
예제 출력 2 
171
예제 입력 3 
12
예제 출력 3 
2731
출처
문제를 만든 사람: baekjoon
"""

import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip("\n")) # 1 <= n <= 1000
    dp = [0] * (1001)
    dp[1] = 1 # l
    dp[2] = 3 # l l, - -, o 
    dp[3] = 5 # l l l, l - -, --1, 1o, ol
    dp[4] = 11 # llll, l--l, --ll, lol, oll, ll--, ----,o--, llo,--0,oo
    dp[5] = 21 # lllll,lll--, l--ll, ll--l,--lll, 1-----,--1--, -----1, 
               # 111o,11o1,1o11,o111, 1o--,1--o,o1--,o--1, --1o, --o1, 1oo, o1o, oo1

    if n >= 6:
        for i in range(6, n+1):
            dp[i] = dp[i-1] + 2*dp[i-2]
            # print(f"{i}: {dp[i]}")

    print(dp[n] % 10007)


if __name__ == '__main__':
    main()
