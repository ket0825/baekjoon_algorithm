"""
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 
이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 
0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. 
N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1 
1
예제 출력 1 
9
예제 입력 2 
2
예제 출력 2 
17
출처
문제를 만든 사람: baekjoon
"""
## 1. dp로 진행하기. shallow copy 조심하기. 괜히 수학적 공식으로 풀려고 하지 말자.
import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip("\n")) # 1 <= N <= 100. length of number line.
    # dp = [[0] * 10] * 101 # 2 cases: 0,9 or not 0,9. This case => shallow copy.
    dp = [[0] * 10 for _ in range(101)] # 2 cases: 0,9 or not 0,9. This case => shallow copy.

    dp[1] = [0]+[1]*9
    
    if N > 1:
        for i in range(2, N+1):
            for j in range(10):
                if j == 0:
                    dp[i][j] = dp[i-1][1]%1000000000
                elif j == 9:
                    dp[i][j] = dp[i-1][8]%1000000000
                else:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%1000000000
            
            # print(f"{dp[i]}, \n sum: {sum(dp[i])}")
            
    print(sum(dp[N])%1000000000)


# if __name__ == '__main__':
#     main()

## 2. 수학적 공식으로 진행하기... 아닌듯.
# import sys
# input = sys.stdin.readline

# def main():
#     N = int(input().rstrip("\n")) # 1 <= N <= 100. length of number line.
#     dp = [0] * 101

#     dp[1] = 9
#     dp[2] = 17
    
#     sample = [0] * 101

#     sample[1] = 9
#     sample[2] = 17
    
#     if N > 2:
#         for i in range(3, N+1):
#             dp[i] = (dp[i-1] * 2 - 2)%1000000000
            
#     print(dp[N]%1000000000)


# if __name__ == '__main__':
#     main()
    
    