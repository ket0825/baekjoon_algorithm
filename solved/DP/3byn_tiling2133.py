"""
타일 채우기
2 초	128 MB
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
## 1. 자연수의 분할 문제처럼 생각.
import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip('\n')) # N(1 ≤ N ≤ 30)

    if N % 2 == 1:
        print(0)
        return
    # 매 순간마다 새로운 패턴이 생김. 2개씩... 
    # 보다 보니 자연수의 분할 문제 같네...?
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


## 2. 재귀적이고, 메모를 해가며 푸는 방식. 출처: shj9801
N = int(input())

pattern = [
  [4, 1, 7],
  [0, 6],
  [5],
  [4],
  [3, 0],
  [2],
  [1],
  [0]
]

memo = [[-1 for j in range(8)] for i in range(N + 1)]

def getAns(idx, curLinePattern):
  if idx == N - 1:
    if curLinePattern == 7 or curLinePattern == 1 or curLinePattern == 4:
      return 1
    else:
      return 0
  
  ans = 0
  for e in pattern[curLinePattern]:
    if memo[idx + 1][e] == -1:
      memo[idx + 1][e] = getAns(idx + 1, e)
    ans += memo[idx + 1][e]
  return ans

print(getAns(0, 0))