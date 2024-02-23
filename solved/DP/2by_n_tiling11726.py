"""
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를
구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 
10,007로 나눈 나머지를 출력한다.

예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
9
예제 출력 2 
55
출처: baekjoon
"""

## 1. dp가 아닌 그냥 규칙을 이용한 풀이.
import sys
input = sys.stdin.readline
import math

def main():
    n = int(input().rstrip("\n")) # 1 <= n <= 1000
    ans = [math.comb(n-i,i) for i in range(n) if n-i >= i]
    print(sum(ans)%10007)
    

if __name__ == "__main__":
    main()


## 2. dp로 풀기.
# n번째는
# n-1은 오른쪽에 2*1,
# n-2는 오른쪽에 2*2 가 붙는다고 생각할 수 있음.
    
import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip("\n")) # 1 <= n <= 1000
    dp = [0]*(1001)

    dp[1] = 1
    dp[2] = 2
    
    if n > 3:
        for i in range(3, 1001):
            dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n]%10007)


if __name__ == "__main__":
    main()
    