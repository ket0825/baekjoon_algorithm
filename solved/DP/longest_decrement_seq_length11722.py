"""
가장 긴 감소하는 부분 수열
1 초	256 MB	34098	21163	17374	62.984%

문제
수열 A가 주어졌을 때, 
가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 
가장 긴 감소하는 부분 수열은 A = {30, 20, 10}  이고, 길이는 3이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 30 10 20 20 10
예제 출력 1 
3
출처
문제를 만든 사람: baekjoon
"""

## 1. nlogn algorithm
import bisect
import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip('\n')) # 1 ≤ N ≤ 1,000
    S = [*map(int, input().rstrip().split(" "))] # 1 ≤ Ai ≤ 1,000
    S = [0]+S[::-1] # 역순으로 만들어서 진행.

    dp = [0]*(N+1)
    dp[1] = S[1]
    length = 1
    if N > 1:
        for i in range(2, N+1):
            if dp[length] < S[i]:
                length+=1
                dp[length] = S[i]
            else:
                idx = bisect.bisect_left(dp, S[i], 1, length)
                dp[idx] = S[i]
    
    print(length)


if __name__ == '__main__':
    main()