"""
타일 채우기
2 초	128 MB	52085	18966	15057	36.329%
문제
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

출력
첫째 줄에 경우의 수를 출력한다.

예제 입력 1 
2
예제 출력 1 
3
"""
## 매 순간마다 새로운 패턴이 생김. 2개씩...
import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip('\n')) # N(1 ≤ N ≤ 30)

    if N % 2 == 1:
        print(0)
        return
    
    # 자연수의 분할 문제 같네...?
    dp = [0]*(N//2+1)
    dp[1] = 3

    if N > 2:
        for i in range(2, N//2 +1):
            dp[i] += dp[i-1]*3
            for j in range(1, i-1):
                dp[i] += dp[j]*2
            dp[i] += 2
        
    print(dp[N//2])


if __name__ == '__main__':
    main()